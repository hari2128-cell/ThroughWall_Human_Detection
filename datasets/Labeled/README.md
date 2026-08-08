# Labeled Recordings

Ground-truth-labeled recordings for tuning and evaluating
`signal_processing/Motion_Detection/detectMotion.m`.

## Naming convention

`<class>_<id>.csv` where `<class>` is `static` (no person present / no
motion) or `motion` (person moving in radar's field of view). This
convention is what `tuneThreshold.m` globs for (`static_*.csv`,
`motion_*.csv`).

## Current contents

5x `static_*.csv` and 5x `motion_*.csv`, 4 seconds each at 1000 Hz —
**synthetically generated** (see `datasets/README.md` for the disclosure).
They let `tuneThreshold.m` and `experiments/Accuracy_Evaluation` run
end-to-end immediately. Replace with real labeled captures from your own
radar hardware for actual placement/evaluation numbers:

1. Record N seconds of a completely static scene → save as `static_XX.csv`
2. Record N seconds with a person walking in the radar's field of view →
   save as `motion_XX.csv`
3. Aim for at least 10-20 recordings per class across different distances
   and (if testing through-wall performance) different wall materials, to
   get a statistically meaningful threshold and accuracy figure.
