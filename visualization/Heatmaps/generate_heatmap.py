#!/usr/bin/env python3
"""
generate_heatmap.py

Offline heatmap generator: reads a recorded CSV (see datasets/), computes a
sliding-window spectrogram, and saves it as a PNG image under
results/Heatmaps/. Complements the live heatmap panel in
visualization/Python_GUI/radar_gui.py and MATLAB's shortTimeFFT.m.

Usage:
    python generate_heatmap.py --input ../../datasets/Sample_Recordings/human_walking.csv \
        --output ../../results/Heatmaps/human_walking_heatmap.png
"""

import argparse

import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt


def short_time_fft(x, fs, window_sec=2.0, hop_sec=0.25):
    window_len = int(fs * window_sec)
    hop_len = int(fs * hop_sec)
    n = len(x)
    num_windows = max(1, (n - window_len) // hop_len + 1)

    spec = []
    times = []
    for w in range(num_windows):
        start = w * hop_len
        end = start + window_len
        if end > n:
            break
        segment = x[start:end]
        windowed = segment * np.hanning(window_len)
        mag = np.abs(np.fft.fft(windowed)[: window_len // 2]) / window_len
        spec.append(mag)
        times.append((start + end) / 2 / fs)

    freqs = np.fft.fftfreq(window_len, d=1.0 / fs)[: window_len // 2]
    return np.array(spec).T, freqs, np.array(times)


def main():
    parser = argparse.ArgumentParser(description="Generate a motion-intensity heatmap from a recording")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--fs", type=int, default=1000)
    args = parser.parse_args()

    x = np.loadtxt(args.input, skiprows=1)
    x = x - np.mean(x)
    nyq = args.fs / 2.0
    b, a = butter(4, [0.5 / nyq, 40 / nyq], btype="bandpass")
    x = filtfilt(b, a, x)

    spec, freqs, times = short_time_fft(x, args.fs)

    plt.figure(figsize=(10, 5))
    plt.imshow(spec, aspect="auto", origin="lower", cmap="hot",
               extent=[times[0], times[-1], freqs[0], freqs[-1]])
    plt.colorbar(label="Magnitude")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.title(f"Motion Intensity Heatmap — {args.input}")
    plt.tight_layout()
    plt.savefig(args.output, dpi=150)
    print(f"Saved heatmap to {args.output}")


if __name__ == "__main__":
    main()
