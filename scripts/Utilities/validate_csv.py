#!/usr/bin/env python3
"""
validate_csv.py

Sanity-checks a recorded radar CSV before feeding it into analysis:
- confirms it has the expected single numeric column
- reports sample count, implied duration (given --fs), min/max/mean values
- flags likely-saturated recordings (values pinned near 0 or 4095, the
  12-bit ADC rails) which usually indicate a wiring problem

Usage:
    python validate_csv.py --input ../../datasets/Raw/human_walking.csv --fs 1000
"""

import argparse

import numpy as np


def main():
    parser = argparse.ArgumentParser(description="Validate a recorded radar CSV")
    parser.add_argument("--input", required=True)
    parser.add_argument("--fs", type=int, default=1000)
    args = parser.parse_args()

    x = np.loadtxt(args.input, skiprows=1)
    n = len(x)
    duration = n / args.fs

    print(f"File: {args.input}")
    print(f"Samples: {n}")
    print(f"Implied duration at {args.fs} Hz: {duration:.2f} s")
    print(f"Min: {x.min():.2f}  Max: {x.max():.2f}  Mean: {x.mean():.2f}  Std: {x.std():.2f}")

    saturated_low = np.mean(x < 10) * 100
    saturated_high = np.mean(x > 4085) * 100
    if saturated_low > 1 or saturated_high > 1:
        print(f"WARNING: {saturated_low:.1f}% of samples near 0 and "
              f"{saturated_high:.1f}% near 4095 — check wiring/radar power, "
              "signal may be clipping.")
    else:
        print("No significant ADC saturation detected.")


if __name__ == "__main__":
    main()
