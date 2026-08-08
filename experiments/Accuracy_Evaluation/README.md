# Experiment: Accuracy Evaluation & Threshold Tuning

## Objective
Quantitatively evaluate `signal_processing/Motion_Detection/detectMotion.m`
against labeled data, and select a good operating threshold.

## Method
Run `signal_processing/Motion_Detection/tuneThreshold.m` (MATLAB) — or the
equivalent Python sweep below — against `datasets/Labeled/` (5x `static_*`,
5x `motion_*`, 4s @ 1000 Hz each). For each candidate threshold, compute:

- **Precision** = TP / (TP + FP)
- **Recall** = TP / (TP + FN)
- **F1** = 2·precision·recall / (precision + recall)

## Results — synthetic labeled dataset (shipped with this repo)

⚠️ These numbers come from the **synthetic** example recordings in
`datasets/Labeled/` (see `datasets/README.md`), not real radar hardware —
they demonstrate the evaluation *method* end-to-end. Re-run this exact
procedure against your own recorded data and replace the table below before
citing these numbers as real system performance.

**Computed band-limited spectral energy per recording:**

| File | Energy |
|---|---|
| static_01.csv | 5.76 |
| static_02.csv | 4.46 |
| static_03.csv | 2.84 |
| static_04.csv | 3.17 |
| static_05.csv | 3.33 |
| motion_01.csv | 8929.29 |
| motion_02.csv | 7844.11 |
| motion_03.csv | 6942.89 |
| motion_04.csv | 12449.23 |
| motion_05.csv | 5726.26 |

**Best threshold found:** ≈ 62.6 (any value between ~6 and ~5726 separates
the classes perfectly in this synthetic set, since static-scene energy is
several orders of magnitude below motion energy by construction)

**Performance at best threshold:**

| Metric | Value |
|---|---|
| Precision | 1.00 |
| Recall | 1.00 |
| F1 score | 1.00 |
| True Positives | 5 |
| False Positives | 0 |
| True Negatives | 5 |
| False Negatives | 0 |

## Interpretation

The perfect separation above is expected and *not* representative of real
hardware — the synthetic motion signal is a clean sine wave with no
sensor noise floor overlap, so it trivially separates from the near-zero
synthetic static energy. **Real radar data will have a much smaller gap**
between static-scene noise-floor energy and genuine motion energy,
especially at longer range or through a wall, so real precision/recall
will be lower than this synthetic ceiling. Expect to iterate:

1. Collect ≥20 labeled recordings per class on real hardware, across your
   target distances/wall materials (see `Different_Walls`, `Distance_Test`).
2. Re-run `tuneThreshold.m` against that real data.
3. Pick the threshold at peak F1, or bias toward higher recall (lower
   threshold) if missed detections are more costly than false alarms for
   your use case (e.g. security applications), or vice versa.
4. Update `motionThresh` in `signal_processing/MATLAB/live_radar_pipeline.m`,
   `visualization/Python_GUI/radar_gui.py`, and
   `signal_processing/Motion_Detection/detectMotion.m`'s default with the
   chosen value, and record the final number here.

## Reproducing this evaluation

```matlab
% MATLAB
addpath(genpath('signal_processing'));
tuneThreshold('datasets/Labeled', 1000);
```

```python
# Python equivalent (ad hoc), using scripts/requirements.txt deps
import glob, numpy as np
from scipy.signal import butter, filtfilt

def energy(path, Fs=1000):
    x = np.loadtxt(path, skiprows=1) - np.mean(np.loadtxt(path, skiprows=1))
    b, a = butter(4, [0.5/(Fs/2), 40/(Fs/2)], btype='bandpass')
    xf = filtfilt(b, a, x)
    N = len(xf)
    mag = np.abs(np.fft.fft(xf*np.hanning(N))[:N//2]) / N
    return np.sum(mag**2)

static_e = [energy(f) for f in sorted(glob.glob('datasets/Labeled/static_*.csv'))]
motion_e = [energy(f) for f in sorted(glob.glob('datasets/Labeled/motion_*.csv'))]
```
