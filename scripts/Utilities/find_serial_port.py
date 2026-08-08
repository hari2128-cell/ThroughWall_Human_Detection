#!/usr/bin/env python3
"""
find_serial_port.py

Lists available serial ports so you can identify which one the ESP32
enumerated as, before running any of the data collection/visualization
scripts. Handy since the port name/number differs across OSes and can
shift between reboots.

Usage:
    python find_serial_port.py
"""

import serial.tools.list_ports


def main():
    ports = list(serial.tools.list_ports.comports())
    if not ports:
        print("No serial ports found. Is the ESP32 plugged in and drivers installed?")
        return

    print(f"Found {len(ports)} serial port(s):\n")
    for p in ports:
        print(f"  {p.device}")
        print(f"    Description : {p.description}")
        print(f"    HWID        : {p.hwid}")
        print()

    print("Tip: an ESP32's USB-UART bridge chip (CP2102/CH340/etc.) usually "
          "shows a matching description above. Use that port name with "
          "--port in the other scripts.")


if __name__ == "__main__":
    main()
