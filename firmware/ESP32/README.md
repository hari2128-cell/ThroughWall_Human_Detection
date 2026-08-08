# ESP32 Firmware

`main/main.ino` samples the radar's analog IF output on GPIO34 at a fixed rate
(default 1000 Hz, configurable via `SAMPLE_RATE_HZ`) and streams each 12-bit
ADC sample as a newline-terminated integer over USB serial at 115200 baud.

## Build & flash

**Arduino IDE**
1. Install the ESP32 board package (Boards Manager → "esp32").
2. Open `main/main.ino`.
3. Select your ESP32 board and port, then Upload.

**PlatformIO**
```bash
cd firmware/ESP32
pio run -t upload
pio device monitor
```

## Notes

- GPIO34 is input-only and ADC1, safe to use while Wi-Fi is active (ADC2 pins
  conflict with Wi-Fi — avoid those for this signal).
- Increase `SAMPLE_RATE_HZ` if you need finer Doppler frequency resolution;
  keep it consistent with the sample rate configured in the MATLAB scripts.
