# Motion Detection

| File | Purpose |
|---|---|
| `detectMotion.m` | Threshold-based classifier: motion detected if band-limited spectral energy exceeds a threshold |
| `tuneThreshold.m` | Sweeps thresholds against labeled static/motion recordings and reports precision/recall/F1 to help pick a good operating point |

## Current approach: fixed energy threshold

Simple, interpretable, and fast enough for real-time use on a laptop. The
threshold (`3.0` default) was chosen as a starting point — **re-tune it for
your own radar module and environment** using `tuneThreshold.m` against
recordings in `datasets/Labeled/`, and record the result in
`experiments/Accuracy_Evaluation`.

## Planned upgrade: ML-based classification

The feature vector produced by `signal_processing/Feature_Extraction`
(energy, peak frequency, spectral centroid, bandwidth) is designed to drop
directly into a simple classifier (e.g. logistic regression, small decision
tree, or SVM) trained on labeled data, to move beyond single-threshold
energy detection and distinguish finer motion classes (walking vs. static
vs. gesture vs. multiple targets). Tracked under Future Improvements in the
top-level README.
