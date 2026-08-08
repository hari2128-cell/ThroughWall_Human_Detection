function y = lowpassFilterSignal(x, Fs, fCutoff, order)
%LOWPASSFILTERSIGNAL Zero-phase Butterworth low-pass filter.
%   y = lowpassFilterSignal(x, Fs, fCutoff, order)
%   Useful in isolation for suppressing high-frequency electrical noise
%   above the motion band, e.g. before further band-limiting.

    if nargin < 3, fCutoff = 40; end
    if nargin < 4, order = 4; end

    fCutoff = min(fCutoff, Fs/2 - 1);
    [b, a] = butter(order, fCutoff / (Fs/2), 'low');
    y = filtfilt(b, a, x);
end
