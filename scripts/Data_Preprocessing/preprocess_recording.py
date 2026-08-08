#!/usr/bin/env python3
"""
preprocess_recording.py

Batch-preprocess raw recordings from datasets/Raw/ into cleaned versions in
datasets/Processed/: DC-offset removal + band-pass filtering, matching the
same processing applied live in visualization/Python_GUI/radar_gui.py and
signal_processing/MATLAB/live_radar_pipeline.m, so processed files are
directly comparable to what the live pipeline "sees".

Usage:
    python preprocess_recording.py --input-dir ../../datasets/Raw \
        --output-dir ../../datasets/Processed
"""

import argparse
import glob
import os

import numpy as np
from scipy.signal import butter, filtfilt


def preprocess(x, fs, low=0.5, high=40.0, order=4):
    x = x - np.mean(x)
    nyq = fs / 2.0
    b, a = butter(order, [low / nyq, high / nyq], btype="bandpass")
    return filtfilt(b, a, x)


def main():
    parser = argparse.ArgumentParser(description="Batch preprocess raw radar recordings")
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--fs", type=int, default=1000)
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    files = sorted(glob.glob(os.path.join(args.input_dir, "*.csv")))

    if not files:
        print(f"No CSV files found in {args.input_dir}")
        return

    for f in files:
        x = np.loadtxt(f, skiprows=1)
        xf = preprocess(x, args.fs)
        out_path = os.path.join(args.output_dir, os.path.basename(f))
        np.savetxt(out_path, xf, fmt="%.4f", header="filtered_sample", comments="")
        print(f"Processed {f} -> {out_path}")


if __name__ == "__main__":
    main()
