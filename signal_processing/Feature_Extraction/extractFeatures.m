function features = extractFeatures(freqs, mag)
%EXTRACTFEATURES Compute a small feature vector from an FFT spectrum,
%suitable as input to threshold-based or (future) ML-based motion
%classifiers.
%
%   features = extractFeatures(freqs, mag)
%
%   features.energy       - total spectral energy (sum of squared magnitudes)
%   features.peakFreqHz   - frequency of the dominant peak
%   features.peakMag      - magnitude of the dominant peak
%   features.centroidHz   - spectral centroid (energy-weighted mean frequency)
%   features.bandwidthHz  - spectral spread around the centroid

    energy = sum(mag.^2);
    [peakMag, idx] = max(mag);
    peakFreq = freqs(idx);

    totalMag = sum(mag) + eps;
    centroid = sum(freqs .* mag) / totalMag;
    bandwidth = sqrt(sum(((freqs - centroid).^2) .* mag) / totalMag);

    features.energy = energy;
    features.peakFreqHz = peakFreq;
    features.peakMag = peakMag;
    features.centroidHz = centroid;
    features.bandwidthHz = bandwidth;
end
