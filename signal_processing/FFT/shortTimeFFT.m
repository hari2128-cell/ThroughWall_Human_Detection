function [S, freqs, times] = shortTimeFFT(x, Fs, windowSec, hopSec)
%SHORTTIMEFFT Compute a sliding-window (short-time) FFT / spectrogram.
%
%   [S, freqs, times] = shortTimeFFT(x, Fs, windowSec, hopSec)
%
%   x         - full-length time-domain signal
%   Fs        - sample rate (Hz)
%   windowSec - analysis window length in seconds (default 2)
%   hopSec    - hop size between successive windows in seconds (default 0.25)
%
%   S      - matrix of magnitude spectra, one column per time step
%   freqs  - frequency bin centers (Hz), rows of S
%   times  - center time (s) of each analysis window, columns of S
%
% Used for generating the motion-intensity heatmap in
% visualization/Heatmaps and results/Heatmaps.

    if nargin < 3, windowSec = 2;    end
    if nargin < 4, hopSec    = 0.25; end

    windowLen = round(Fs * windowSec);
    hopLen    = round(Fs * hopSec);
    x = x(:);
    N = numel(x);

    numWindows = max(1, floor((N - windowLen) / hopLen) + 1);
    S = zeros(floor(windowLen/2), numWindows);
    times = zeros(1, numWindows);

    for w = 1:numWindows
        startIdx = (w-1)*hopLen + 1;
        endIdx = startIdx + windowLen - 1;
        if endIdx > N
            break;
        end
        segment = x(startIdx:endIdx);
        [freqs, mag] = computeFFT(segment, Fs);
        S(:, w) = mag;
        times(w) = (startIdx + endIdx) / 2 / Fs;
    end
end
