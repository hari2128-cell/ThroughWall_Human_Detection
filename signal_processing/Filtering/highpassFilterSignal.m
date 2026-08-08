function y = highpassFilterSignal(x, Fs, fCutoff, order)
%HIGHPASSFILTERSIGNAL Zero-phase Butterworth high-pass filter.
%   y = highpassFilterSignal(x, Fs, fCutoff, order)
%   Useful in isolation for rejecting DC offset and slow drift, as an
%   alternative to removeDCOffset.m when drift is non-constant over time.

    if nargin < 3, fCutoff = 0.5; end
    if nargin < 4, order = 4; end

    fCutoff = max(fCutoff, 1e-3);
    [b, a] = butter(order, fCutoff / (Fs/2), 'high');
    y = filtfilt(b, a, x);
end
