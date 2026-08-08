#!/usr/bin/env python3
"""
quick_plot.py

Fast static (non-interactive) plot of a recorded CSV: raw signal, filtered
signal, and FFT spectrum, saved as a single PNG. Useful for quickly
generating a figure for a report/presentation without launching the full
interactive GUI.

Usage:
    python quick_plot.py --input ../../datasets/Raw/human_walking.csv \
        --output ../../results/Graphs/human_walking_quicklook.png
"""

import argparse

import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser(description="Quick static plot of a recorded CSV")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--fs", type=int, default=1000)
    args = parser.parse_args()

    x = np.loadtxt(args.input, skiprows=1)
    x = x - np.mean(x)
    nyq = args.fs / 2.0
    b, a = butter(4, [0.5 / nyq, 40 / nyq], btype="bandpass")
    xf = filtfilt(b, a, x)

    n = len(xf)
    mag = np.abs(np.fft.fft(xf * np.hanning(n))[: n // 2]) / n
    freqs = np.fft.fftfreq(n, d=1.0 / args.fs)[: n // 2]

    fig, axes = plt.subplots(3, 1, figsize=(9, 8))
    t = np.arange(len(x)) / args.fs

    axes[0].plot(t, x)
    axes[0].set_title("Raw Signal (DC removed)")
    axes[0].set_xlabel("Time (s)")

    axes[1].plot(t, xf)
    axes[1].set_title("Band-pass Filtered Signal")
    axes[1].set_xlabel("Time (s)")

    axes[2].plot(freqs, mag)
    axes[2].set_title("Frequency Spectrum (FFT)")
    axes[2].set_xlabel("Frequency (Hz)")

    plt.tight_layout()
    plt.savefig(args.output, dpi=150)
    print(f"Saved plot to {args.output}")
    print(f"Band energy (0.5-40Hz): {np.sum(mag**2):.4f}")


if __name__ == "__main__":
    main()
