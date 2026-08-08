function [detected, energy] = detectMotion(mag, thresh)
%DETECTMOTION Simple threshold-based motion classifier.
%
%   [detected, energy] = detectMotion(mag, thresh)
%
%   mag    - FFT magnitude spectrum (band-limited to the motion band)
%   thresh - energy threshold above which motion is declared (default 3.0)
%
%   detected - logical, true if energy > thresh
%   energy   - the computed spectral energy (sum of squared magnitudes),
%              useful for logging/tuning the threshold
%
% See experiments/Accuracy_Evaluation for how `thresh` was tuned against
% labeled static vs. human-motion recordings (ROC-style sweep).

    if nargin < 2
        thresh = 3.0;
    end
    energy = sum(mag.^2);
    detected = energy > thresh;
end
