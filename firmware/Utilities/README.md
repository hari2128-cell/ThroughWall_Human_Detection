# Utilities

Small, reusable firmware helpers that don't belong to a specific hardware
driver or communication layer.

- `SampleTimer.h` — non-blocking fixed-rate scheduler (`isDue()` polling
  pattern) used to trigger ADC reads at a precise rate without `delay()`,
  keeping the serial-drain loop responsive. This is the same logic used
  inline in `main/main.ino`; use this class instead if you refactor the
  sketch into multiple files.

Add here: logging helpers, config/EEPROM helpers, debug print macros, etc.
as the project grows.
