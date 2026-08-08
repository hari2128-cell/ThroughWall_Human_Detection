# include/

PlatformIO convention folder for project-wide header files that aren't
tied to a specific library. Currently the modular headers live in the
top-level `firmware/Drivers`, `firmware/Sensor_Interface`,
`firmware/Communication`, and `firmware/Utilities` folders so they can be
shared with the native unit tests in `firmware/Tests`.

If you refactor `main/main.ino` to use those classes, copy or symlink the
headers you need into this folder (PlatformIO auto-adds `include/` to the
compiler search path), e.g.:

```bash
cp ../../Drivers/RadarSensor.h .
cp ../../Sensor_Interface/SampleBuffer.h .
cp ../../Communication/SerialStreamer.h .
cp ../../Utilities/SampleTimer.h .
```
