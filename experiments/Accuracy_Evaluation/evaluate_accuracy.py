#!/usr/bin/env python3
"""
evaluate_accuracy.py

Python equivalent of signal_processing/Motion_Detection/tuneThreshold.m —
sweeps energy thresholds against datasets/Labeled/ (static_*.csv,
motion_*.csv) and reports precision/recall/F1 for each, plus the
best-F1 threshold.

Usage:
    python evaluate_accuracy.py --labeled-dir ../../datasets/Labeled --fs 1000
"""

import argparse
import glob
import os

import numpy as np
from scipy.signal import butter, filtfilt


def band_energy(path, fs, low=0.5, high=40.0, order=4):
    x = np.loadtxt(path, skiprows=1)
    x = x - np.mean(x)
    nyq = fs / 2.0
    b, a = butter(order, [low / nyq, high / nyq], btype="bandpass")
    xf = filtfilt(b, a, x)
    n = len(xf)
    mag = np.abs(np.fft.fft(xf * np.hanning(n))[: n // 2]) / n
    return float(np.sum(mag**2))


def main():
    parser = argparse.ArgumentParser(description="Evaluate motion-detection threshold accuracy")
    parser.add_argument("--labeled-dir", default=os.path.join("..", "..", "datasets", "Labeled"))
    parser.add_argument("--fs", type=int, default=1000)
    parser.add_argument("--steps", type=int, default=200)
    args = parser.parse_args()

    static_files = sorted(glob.glob(os.path.join(args.labeled_dir, "static_*.csv")))
    motion_files = sorted(glob.glob(os.path.join(args.labeled_dir, "motion_*.csv")))

    if not static_files or not motion_files:
        print(f"No labeled files found in {args.labeled_dir}. "
              "Expected static_*.csv and motion_*.csv.")
        return

    static_e = [band_energy(f, args.fs) for f in static_files]
    motion_e = [band_energy(f, args.fs) for f in motion_files]

    print("Static energies:", [round(e, 4) for e in static_e])
    print("Motion energies:", [round(e, 4) for e in motion_e])

    best = None
    max_e = max(static_e + motion_e)
    for t in np.linspace(0, max_e, args.steps):
        tp = sum(e > t for e in motion_e)
        fn = sum(e <= t for e in motion_e)
        fp = sum(e > t for e in static_e)
        tn = sum(e <= t for e in static_e)
        precision = tp / max(tp + fp, 1)
        recall = tp / max(tp + fn, 1)
        f1 = 2 * precision * recall / max(precision + recall, 1e-9)
        if best is None or f1 > best["f1"]:
            best = dict(threshold=t, precision=precision, recall=recall, f1=f1,
                        tp=tp, fp=fp, tn=tn, fn=fn)

    print("\nBest threshold:")
    for k, v in best.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
