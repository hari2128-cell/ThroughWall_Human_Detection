%% analyze_recording.m
% Offline analysis of a recorded radar CSV file (one ADC sample per line).
% Useful for experiments/ subfolders (e.g. Static_Object, Human_Motion,
% Different_Walls) where data was logged with scripts/Data_Collection.
%
% Usage:
%   analyze_recording('datasets/Raw/human_motion_trial1.csv', 1000)

function analyze_recording(csvPath, Fs)
    if nargin < 2
        Fs = 1000;
    end

    data = readmatrix(csvPath);
    x = data(:,1);

    x = x - mean(x);                          % DC offset removal
    [b, a] = butter(4, [0.5 40] / (Fs/2), 'bandpass');
    xFiltered = filtfilt(b, a, x);

    N = numel(xFiltered);
    X = fft(xFiltered .* hann(N));
    mag = abs(X(1:floor(N/2))) / N;
    freqs = (0:floor(N/2)-1) * (Fs/N);

    figure('Name', ['Analysis: ' csvPath], 'NumberTitle', 'off');

    subplot(3,1,1);
    plot((0:N-1)/Fs, x); title('Raw Signal (DC removed)');
    xlabel('Time (s)'); ylabel('Amplitude');

    subplot(3,1,2);
    plot((0:N-1)/Fs, xFiltered); title('Band-pass Filtered Signal');
    xlabel('Time (s)'); ylabel('Amplitude');

    subplot(3,1,3);
    plot(freqs, mag); title('Frequency Spectrum (FFT)');
    xlabel('Frequency (Hz)'); ylabel('|X(f)|');

    energy = sum(mag.^2);
    fprintf('Signal energy in 0.5-40 Hz band: %.4f\n', energy);
end
