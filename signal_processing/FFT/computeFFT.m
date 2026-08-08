function [freqs, mag] = computeFFT(x, Fs)
%COMPUTEFFT Windowed single-sided FFT magnitude spectrum.
%
%   [freqs, mag] = computeFFT(x, Fs)
%
%   x    - time-domain signal (column vector), ideally already filtered
%   Fs   - sample rate (Hz)
%
%   freqs - frequency bin centers, 0 .. Fs/2 (Hz)
%   mag   - magnitude at each frequency bin (single-sided, normalized by N)
%
% Applies a Hann window before the FFT to reduce spectral leakage from the
% finite analysis window, which otherwise smears energy across
% neighboring frequency bins and can mask a genuine but weak Doppler peak.

    N = numel(x);
    X = fft(x(:) .* hann(N));
    mag = abs(X(1:floor(N/2))) / N;
    freqs = (0:floor(N/2)-1)' * (Fs/N);
end
