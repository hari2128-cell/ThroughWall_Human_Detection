#!/usr/bin/env python3
"""
terminal_dashboard.py

Lightweight live monitoring option for headless environments (e.g. a
Raspberry Pi driving the ESP32 without a display attached, or SSH-only
access): prints a scrolling text dashboard of motion status and energy to
the terminal instead of a matplotlib GUI. Useful as a fallback for
visualization/Python_GUI/radar_gui.py, or as a systemd-service-friendly
monitor.

Usage:
    python terminal_dashboard.py --port /dev/ttyUSB0
"""

import argparse
import collections
import shutil
import time

import numpy as np
import serial
from scipy.signal import butter, filtfilt

FS = 1000
WINDOW_SEC = 2
WINDOW_LEN = FS * WINDOW_SEC
MOTION_THRESH = 3.0


def band_energy(x, fs):
    x = x - np.mean(x)
    nyq = fs / 2.0
    b, a = butter(4, [0.5 / nyq, 40 / nyq], btype="bandpass")
    xf = filtfilt(b, a, x)
    n = len(xf)
    mag = np.abs(np.fft.fft(xf * np.hanning(n))[: n // 2]) / n
    return float(np.sum(mag**2))


def bar(value, max_value, width=40):
    filled = int(min(value / max_value, 1.0) * width) if max_value > 0 else 0
    return "#" * filled + "-" * (width - filled)


def main():
    parser = argparse.ArgumentParser(description="Terminal-based live radar monitor")
    parser.add_argument("--port", required=True)
    parser.add_argument("--baud", type=int, default=115200)
    parser.add_argument("--threshold", type=float, default=MOTION_THRESH)
    args = parser.parse_args()

    ser = serial.Serial(args.port, args.baud, timeout=1)
    buffer = collections.deque([0.0] * WINDOW_LEN, maxlen=WINDOW_LEN)

    print("Live radar monitor — Ctrl+C to stop\n")
    try:
        while True:
            while ser.in_waiting:
                line = ser.readline().decode("utf-8", errors="ignore").strip()
                if not line or line.startswith("#"):
                    continue
                try:
                    buffer.append(float(line))
                except ValueError:
                    continue

            energy = band_energy(np.array(buffer), FS)
            status = "MOTION DETECTED" if energy > args.threshold else "no motion     "
            width = shutil.get_terminal_size((80, 20)).columns - 30
            print(f"\r{status} | energy={energy:8.2f} [{bar(energy, args.threshold*3, max(width,10))}]", end="")
            time.sleep(0.25)
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        ser.close()


if __name__ == "__main__":
    main()
