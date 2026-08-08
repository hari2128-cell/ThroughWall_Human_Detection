#!/usr/bin/env python3
"""
record_serial_to_csv.py

Reads ADC samples streamed by the ESP32 radar firmware over serial and
saves them to a CSV file for offline MATLAB analysis (see
signal_processing/MATLAB/analyze_recording.m).

Usage:
    python record_serial_to_csv.py --port /dev/ttyUSB0 --baud 115200 \
        --duration 30 --out ../../datasets/Raw/human_motion_trial1.csv
"""

import argparse
import csv
import time

import serial


def main():
    parser = argparse.ArgumentParser(description="Record radar ADC samples to CSV")
    parser.add_argument("--port", required=True, help="Serial port, e.g. COM3 or /dev/ttyUSB0")
    parser.add_argument("--baud", type=int, default=115200)
    parser.add_argument("--duration", type=float, default=30.0, help="Recording length in seconds")
    parser.add_argument("--out", required=True, help="Output CSV file path")
    args = parser.parse_args()

    ser = serial.Serial(args.port, args.baud, timeout=1)
    time.sleep(2)  # allow ESP32 to reset after opening the port
    ser.reset_input_buffer()

    print(f"Recording for {args.duration}s from {args.port} -> {args.out}")
    start = time.time()
    samples = []

    while time.time() - start < args.duration:
        line = ser.readline().decode("utf-8", errors="ignore").strip()
        if not line or line.startswith("#"):
            continue
        try:
            samples.append(int(line))
        except ValueError:
            continue

    ser.close()

    with open(args.out, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["adc_sample"])
        for s in samples:
            writer.writerow([s])

    print(f"Saved {len(samples)} samples to {args.out}")


if __name__ == "__main__":
    main()
