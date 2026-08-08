# Sensor Interface

Mid-level code that connects the low-level `Drivers/RadarSensor` to the rest
of the firmware:

- `SampleBuffer.h` — templated fixed-size ring buffer used to decouple
  fixed-rate ADC sampling (in the main loop) from UART transmission timing.
  `main/main.ino` currently implements this pattern inline; swap in this
  reusable template if you split the sketch into multiple files.

## Example usage

```cpp
#include "SampleBuffer.h"
#include "RadarSensor.h"

RadarSensor radar(34);
SampleBuffer<64> buffer;

void setup() {
  radar.begin();
  Serial.begin(115200);
}

void loop() {
  buffer.push(radar.readRaw());

  uint16_t v;
  while (buffer.pop(v)) {
    Serial.println(v);
  }
}
```
