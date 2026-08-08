# Drivers

Low-level hardware abstraction code.

- `RadarSensor.h` — thin wrapper around ESP32 ADC configuration/reads for the
  radar's analog IF output. Used by `firmware/Sensor_Interface` and can be
  included directly in `firmware/ESP32/main/main.ino` if you refactor the
  sketch to use it instead of raw `analogRead()` calls.

Add drivers here for any additional hardware you integrate later (e.g. an
SD card logger, external ADC, or status LEDs).
