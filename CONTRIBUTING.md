# Contributing

Thanks for your interest in improving this project!

## Getting started

1. Fork the repository and clone your fork.
2. Create a feature branch: `git checkout -b feature/my-improvement`.
3. Make your changes (firmware, MATLAB scripts, docs, etc.).
4. Test:
   - Firmware: flash to an ESP32 and confirm serial output looks sane.
   - MATLAB scripts: run against a sample recording in `datasets/Sample_Recordings/`.
5. Commit with a clear message and open a pull request.

## Areas for contribution

- Improved noise-filtering methods (`signal_processing/Filtering`, `Noise_Removal`)
- Better motion-detection algorithms, incl. ML-based classification
- Multi-target detection / distance estimation
- Wi-Fi/MQTT wireless streaming firmware variant
- Python real-time GUI (`visualization/Python_GUI`)
- Additional wall-material experiments (`experiments/Different_Walls`)

## Code style

- C++/Arduino: follow existing formatting in `firmware/ESP32/main/main.ino`.
- MATLAB: use descriptive function names and comment each processing stage.
- Python: PEP 8, type hints where practical.

## Reporting issues

Please include: hardware used, radar module model, firmware version, and
(if applicable) a short sample recording that reproduces the issue.
