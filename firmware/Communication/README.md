# Communication

Handles the link between the ESP32 and the host PC.

## Current implementation: USB UART

- `SerialStreamer.h` — thin wrapper around `HardwareSerial` implementing the
  project's simple text protocol (comment lines prefixed `#`, one integer
  sample per line).
- Baud rate: 115200 (configurable in `firmware/ESP32/main/main.ino`).
- Parsed on the host side by `signal_processing/MATLAB/live_radar_pipeline.m`
  and `scripts/Data_Collection/record_serial_to_csv.py`.

## Planned: wireless streaming (see Future Improvements)

For a cable-free deployment, this folder is the place to add:
- `WiFiStreamer.h` — stream samples over a TCP/WebSocket connection
- `MqttStreamer.h` — publish samples/detections to an MQTT broker for
  integration with home-automation systems (Home Assistant, Node-RED, etc.)

Keep the same "one sample per message" semantics so downstream MATLAB/Python
parsers require minimal changes when switching transport.
