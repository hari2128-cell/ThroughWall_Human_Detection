# Feature Extraction

## `extractFeatures.m`

Reduces a full FFT spectrum down to a small, interpretable feature vector:

| Feature | Meaning |
|---|---|
| `energy` | Total spectral energy — the primary signal used by the current threshold-based detector in `Motion_Detection` |
| `peakFreqHz` | Frequency of the strongest component — fed into `Doppler_Analysis` for speed estimation |
| `peakMag` | Magnitude of that peak — indicates reflection strength / proximity |
| `centroidHz` | Energy-weighted mean frequency — a single number summarizing "how fast, on average" |
| `bandwidthHz` | Spread of energy around the centroid — wider bandwidth can indicate multiple targets or gestural (non-uniform-speed) motion |

## Why this matters for the roadmap

The current system (see `Motion_Detection`) makes its decision from `energy`
alone via a fixed threshold. This feature set is deliberately broader than
that so it can be reused directly as the input vector for a future
ML-based classifier (e.g. a small decision tree or logistic regression
distinguishing "walking," "static," "gesture," "no target") without
re-deriving spectral statistics — see Future Improvements in the top-level
README.
