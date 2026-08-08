function y = bandpassFilterSignal(x, Fs, fLow, fHigh, order)
%BANDPASSFILTERSIGNAL Zero-phase Butterworth band-pass filter.
%
%   y = bandpassFilterSignal(x, Fs, fLow, fHigh, order)
%
%   x     - input signal (column vector)
%   Fs    - sample rate (Hz)
%   fLow  - lower cutoff frequency (Hz), default 0.5
%   fHigh - upper cutoff frequency (Hz), default 40
%   order - filter order, default 4
%
% Isolates the frequency band where human-motion-induced Doppler shifts
% typically fall (roughly 0.5-40 Hz for walking-speed targets at X-band),
% rejecting DC drift below and electrical/mechanical noise above.
% Uses filtfilt for zero-phase distortion (important for preserving the
% time-domain shape of motion events).

    if nargin < 3, fLow  = 0.5; end
    if nargin < 4, fHigh = 40;  end
    if nargin < 5, order = 4;   end

    fLow  = max(fLow, 1e-3);
    fHigh = min(fHigh, Fs/2 - 1);

    [b, a] = butter(order, [fLow fHigh] / (Fs/2), 'bandpass');
    y = filtfilt(b, a, x);
end
