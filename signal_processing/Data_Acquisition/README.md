# Data Acquisition

Code responsible for getting raw radar samples from the ESP32 into
MATLAB/Python.

- `acquireSamples.m` — reads and parses new integer samples from an open
  `serialport` connection, skipping `#`-prefixed comment/header lines sent
  by the firmware. Used by `signal_processing/MATLAB/live_radar_pipeline.m`.

For offline analysis of previously recorded data, see
`scripts/Data_Collection/record_serial_to_csv.py` (records live serial data
to CSV) and `signal_processing/MATLAB/analyze_recording.m` (analyzes a saved
CSV).

## Sampling parameters

| Parameter | Value | Where configured |
|---|---|---|
| Sample rate | 1000 Hz | `firmware/ESP32/main/main.ino` (`SAMPLE_RATE_HZ`), must match `Fs` in MATLAB scripts |
| ADC resolution | 12-bit | `firmware/ESP32/main/main.ino` (`ADC_RESOLUTION`) |
| Serial baud | 115200 | Firmware and all host scripts |
