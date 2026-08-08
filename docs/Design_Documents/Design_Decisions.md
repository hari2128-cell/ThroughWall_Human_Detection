# Design Documents

## Design goals

| Goal | Target | Rationale |
|---|---|---|
| Sampling rate | 1000 Hz | Comfortably above 2x the highest expected Doppler frequency (~40-80 Hz walking pace at X-band) |
| ADC resolution | 12-bit (ESP32 native) | Sufficient dynamic range for typical radar IF output (0-3.3V) without an external ADC |
| Detection latency | < 0.5 s | 2s sliding window, 0.25s hop gives near-real-time updates |
| False positive rate | Minimized via 0.5-40 Hz band-pass + energy threshold | Rejects DC drift and mains/electrical noise outside the human-motion band |
| Cost | Low-cost, off-the-shelf | ESP32 (~$5), CW Doppler module (~$3-10) |

## Design decisions & trade-offs

1. **Analog IF output over digital radar module** — simplicity and cost;
   trade-off is no built-in range/angle info (single moving-target
   detection only). FMCW upgrade path noted under Future Improvements.
2. **Fixed-rate polling ADC sampling (`micros()` scheduling) instead of a
   hardware timer ISR + DMA** — simpler and accurate enough at 1 kHz; noted
   as a firmware improvement for higher sample rates.
3. **MATLAB for signal processing** — built-in FFT/filter design tooling;
   the same pipeline is mirrored in `visualization/Python_GUI` for anyone
   without a MATLAB license.
4. **UART over Wi-Fi/BLE for v1** — simplest, most reliable real-time link
   for development; wireless streaming (MQTT/Wi-Fi) is a Future Improvement.

## Interface design

- **Radar → ESP32**: single analog wire (IF output) into GPIO34 (ADC1_CH6),
  shared GND, radar VCC per module datasheet.
- **ESP32 → Host PC**: USB-UART, 115200 baud, one integer sample per line;
  `#`-prefixed comment/header lines ignored by parsers.
- **Host PC → User**: MATLAB or Python plots (waveform, spectrum, heatmap),
  optionally logged to CSV in `datasets/Raw/`.

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-07-17 | Initial design: single-target Doppler detection over UART |
| 1.1 | 2026-08-08 | Modularized firmware and signal-processing code into per-stage folders; added tests |
