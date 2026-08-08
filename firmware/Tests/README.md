# Tests

Firmware logic that doesn't touch hardware registers (buffers, timers) can
be unit tested off-target using PlatformIO's native test runner, which
compiles and runs on your dev machine instead of the ESP32.

## test_sample_buffer.cpp

Tests `firmware/Sensor_Interface/SampleBuffer.h` push/pop/full/empty
behavior.

### Running

```bash
cd firmware/ESP32
pio test -e native
```

(Requires a `[env:native]` section in `platformio.ini` with
`platform = native`; add one if not already present, and add
`test_sample_buffer.cpp` to a `test/` directory per PlatformIO conventions,
or run it as a standalone `g++` compile as shown below for a quick check
without PlatformIO.)

### Quick standalone check (no PlatformIO required)

```bash
g++ -std=c++17 -I ../Sensor_Interface -DARDUINO_STUB test_sample_buffer.cpp -o test_sample_buffer
./test_sample_buffer
```

Note: `SampleBuffer.h` includes `<Arduino.h>` for `uint16_t`/`size_t` types;
for a pure off-target build, stub these types via `-DARDUINO_STUB` and a
small shim header, or test the logic by copying the template body into a
plain C++ header without the Arduino dependency. See `test_sample_buffer.cpp`
for the stubbing pattern.
