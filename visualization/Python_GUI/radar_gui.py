#!/usr/bin/env python3
"""
radar_gui.py

Real-time Python alternative to the MATLAB live pipeline, for users without
a MATLAB license. Reads samples from the ESP32 over serial, filters,
computes FFT, applies threshold-based motion detection, and plots the
waveform, spectrum, and a scrolling heatmap using matplotlib.

Usage:
    python radar_gui.py --port /dev/ttyUSB0 --baud 115200

Dependencies: see scripts/requirements.txt (pyserial, numpy, matplotlib)
"""

import argparse
import collections

import numpy as np
import serial
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

FS = 1000            # sample rate, must match firmware SAMPLE_RATE_HZ
WINDOW_SEC = 2
WINDOW_LEN = FS * WINDOW_SEC
MOTION_THRESH = 3.0
HEATMAP_COLS = 120


def bandpass(x, fs, low=0.5, high=40.0, order=4):
    nyq = fs / 2.0
    b, a = butter(order, [low / nyq, high / nyq], btype="bandpass")
    return filtfilt(b, a, x)


def compute_fft(x, fs):
    n = len(x)
    windowed = x * np.hanning(n)
    spectrum = np.fft.fft(windowed)
    mag = np.abs(spectrum[: n // 2]) / n
    freqs = np.fft.fftfreq(n, d=1.0 / fs)[: n // 2]
    return freqs, mag


def main():
    parser = argparse.ArgumentParser(description="Live radar motion-detection GUI")
    parser.add_argument("--port", required=True)
    parser.add_argument("--baud", type=int, default=115200)
    args = parser.parse_args()

    ser = serial.Serial(args.port, args.baud, timeout=1)

    buffer = collections.deque([0.0] * WINDOW_LEN, maxlen=WINDOW_LEN)
    heatmap = np.zeros((FS // 2, HEATMAP_COLS))

    fig, (ax_wave, ax_spec, ax_heat) = plt.subplots(3, 1, figsize=(8, 9))
    (line_wave,) = ax_wave.plot(np.arange(WINDOW_LEN) / FS, np.zeros(WINDOW_LEN))
    ax_wave.set_title("Filtered Time-Domain Signal")
    ax_wave.set_xlabel("Time (s)")

    (line_spec,) = ax_spec.plot(np.zeros(WINDOW_LEN // 2), np.zeros(WINDOW_LEN // 2))
    ax_spec.set_title("Frequency Spectrum (FFT)")
    ax_spec.set_xlabel("Frequency (Hz)")
    ax_spec.set_xlim(0, FS / 2)

    im_heat = ax_heat.imshow(heatmap, aspect="auto", origin="lower", cmap="hot")
    ax_heat.set_title("Motion Intensity Heatmap")

    def update(_frame):
        while ser.in_waiting:
            line = ser.readline().decode("utf-8", errors="ignore").strip()
            if not line or line.startswith("#"):
                continue
            try:
                buffer.append(float(line))
            except ValueError:
                continue

        x = np.array(buffer) - np.mean(buffer)
        try:
            x = bandpass(x, FS)
        except ValueError:
            return line_wave, line_spec, im_heat

        freqs, mag = compute_fft(x, FS)
        energy = float(np.sum(mag**2))
        detected = energy > MOTION_THRESH

        line_wave.set_ydata(x)
        ax_wave.set_ylim(x.min() - 1, x.max() + 1)
        line_spec.set_xdata(freqs)
        line_spec.set_ydata(mag)
        ax_spec.set_ylim(0, max(mag.max() * 1.2, 1e-6))

        nonlocal heatmap
        col = np.zeros((FS // 2, 1))
        n = min(len(mag), FS // 2)
        col[:n, 0] = mag[:n]
        heatmap = np.hstack([heatmap[:, 1:], col])
        im_heat.set_data(heatmap)
        im_heat.set_clim(0, heatmap.max() if heatmap.max() > 0 else 1)

        status = "MOTION DETECTED" if detected else "no motion"
        ax_wave.set_title(f"Filtered Signal — {status} (energy={energy:.2f})")

        return line_wave, line_spec, im_heat

    ani = animation.FuncAnimation(fig, update, interval=250, blit=False)
    plt.tight_layout()
    plt.show()

    ser.close()


if __name__ == "__main__":
    main()
