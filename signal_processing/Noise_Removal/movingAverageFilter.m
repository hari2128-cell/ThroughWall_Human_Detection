function y = movingAverageFilter(x, windowSize)
%MOVINGAVERAGEFILTER Simple moving-average smoothing filter.
%
%   y = movingAverageFilter(x, windowSize)
%
% A cheap way to suppress high-frequency electrical/ADC noise before
% band-pass filtering. Not used in the default live pipeline (which relies
% on the Butterworth band-pass alone), but useful for quick-look plots or
% as a lightweight alternative on more constrained hardware/software.

    if nargin < 2
        windowSize = 5;
    end
    kernel = ones(windowSize, 1) / windowSize;
    y = conv(x, kernel, 'same');
end
