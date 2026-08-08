function y = removeDCOffset(x)
%REMOVEDCOFFSET Subtract the mean of the signal to remove DC bias.
%
%   y = removeDCOffset(x)
%
% The radar's IF output rides on a DC bias set by the module's internal
% mixer/bias network. Removing it prevents the DC component from
% dominating the FFT (a huge spike at 0 Hz) and improves band-pass filter
% behavior downstream.

    y = x - mean(x);
end
