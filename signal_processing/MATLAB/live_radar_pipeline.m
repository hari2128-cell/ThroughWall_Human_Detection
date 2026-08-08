%% live_radar_pipeline.m
% Through-Wall Human Motion Detection - live acquisition + processing pipeline
%
% Reads ADC samples streamed by the ESP32 firmware over serial, removes
% DC offset, band-pass filters the signal, computes a sliding-window FFT,
% applies threshold-based motion detection, and plots:
%   1) live time-domain waveform
%   2) frequency spectrum
%   3) scrolling motion-intensity heatmap
%
% Requires: Instrument Control Toolbox (serialport) - MATLAB R2019b+

clear; close all; clc;

%% ---- User configuration ----
port          = "COM3";      % change to your ESP32 port, e.g. "/dev/ttyUSB0"
baud          = 115200;
Fs            = 1000;        % must match SAMPLE_RATE_HZ in firmware
windowSec     = 2;            % analysis window length (s)
windowLen     = Fs * windowSec;
hopLen        = round(Fs * 0.25); % update every 0.25 s
motionThresh  = 3.0;          % detection threshold, tune experimentally
heatmapCols   = 120;          % scrolling heatmap history length

%% ---- Set up serial connection ----
sp = serialport(port, baud);
configureTerminator(sp, "LF");
flush(sp);

buffer = zeros(windowLen, 1);
heatmapBuffer = zeros(round(Fs/2), heatmapCols); % freq bins x time

fig = figure('Name', 'Through-Wall Motion Detection', 'NumberTitle', 'off');

axWave = subplot(3,1,1);
hWave = plot(axWave, (1:windowLen)/Fs, buffer);
title(axWave, 'Filtered Time-Domain Signal'); xlabel('Time (s)'); ylabel('Amplitude');

axSpec = subplot(3,1,2);
hSpec = plot(axSpec, linspace(0, Fs/2, windowLen/2), zeros(windowLen/2,1));
title(axSpec, 'Frequency Spectrum (FFT)'); xlabel('Frequency (Hz)'); ylabel('|X(f)|');

axHeat = subplot(3,1,3);
hHeat = imagesc(axHeat, heatmapBuffer);
axis(axHeat, 'xy'); colormap(axHeat, 'hot'); colorbar(axHeat);
title(axHeat, 'Motion Intensity Heatmap'); xlabel('Time (windows)'); ylabel('Frequency bin');

disp('Starting live acquisition. Close the figure window to stop.');

while isvalid(fig)
    newSamples = readNewSamples(sp, hopLen);
    if isempty(newSamples)
        continue;
    end

    % Slide the buffer and append new samples
    n = numel(newSamples);
    buffer = [buffer(n+1:end); newSamples];

    % ---- Filtering ----
    filtered = removeDCOffset(buffer);
    filtered = bandpassFilterSignal(filtered, Fs, 0.5, 40); % motion-relevant band

    % ---- FFT ----
    [freqs, mag] = computeFFT(filtered, Fs);

    % ---- Motion detection ----
    [motionDetected, energy] = detectMotion(mag, motionThresh);

    % ---- Update heatmap history ----
    binCount = min(numel(mag), size(heatmapBuffer,1));
    heatmapBuffer = [heatmapBuffer(:,2:end), [mag(1:binCount); zeros(size(heatmapBuffer,1)-binCount,1)]];

    % ---- Plot updates ----
    set(hWave, 'YData', filtered);
    set(hSpec, 'XData', freqs, 'YData', mag);
    set(hHeat, 'CData', heatmapBuffer);

    if motionDetected
        title(axWave, sprintf('Filtered Signal — MOTION DETECTED (energy=%.2f)', energy), 'Color', 'r');
    else
        title(axWave, sprintf('Filtered Signal — no motion (energy=%.2f)', energy), 'Color', 'k');
    end

    drawnow limitrate;
end

clear sp;
disp('Acquisition stopped.');

%% ---------------- Local functions ----------------

function samples = readNewSamples(sp, maxCount)
    samples = [];
    n = sp.NumBytesAvailable;
    if n == 0
        return;
    end
    count = 0;
    while sp.NumBytesAvailable > 0 && count < maxCount
        line = readline(sp);
        line = strtrim(line);
        if startsWith(line, "#") || isempty(line)
            continue; % skip comment/header lines from firmware
        end
        val = str2double(line);
        if ~isnan(val)
            samples(end+1,1) = val; %#ok<AGROW>
            count = count + 1;
        end
    end
end

function y = removeDCOffset(x)
    y = x - mean(x);
end

function y = bandpassFilterSignal(x, Fs, fLow, fHigh)
    fLow  = max(fLow, 1e-3);
    fHigh = min(fHigh, Fs/2 - 1);
    [b, a] = butter(4, [fLow fHigh] / (Fs/2), 'bandpass');
    y = filtfilt(b, a, x);
end

function [freqs, mag] = computeFFT(x, Fs)
    N = numel(x);
    X = fft(x .* hann(N));
    mag = abs(X(1:floor(N/2))) / N;
    freqs = (0:floor(N/2)-1) * (Fs/N);
end

function [detected, energy] = detectMotion(mag, thresh)
    energy = sum(mag.^2);
    detected = energy > thresh;
end
