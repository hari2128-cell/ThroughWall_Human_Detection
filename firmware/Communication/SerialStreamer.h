/*
 * SerialStreamer.h
 * Small helper for streaming radar samples over UART in a consistent,
 * parser-friendly text protocol:
 *   - comment/header lines prefixed with '#'
 *   - one unsigned integer sample per line otherwise
 *
 * Kept deliberately simple (plain text, not binary) so it can be read by
 * MATLAB's serialport(), Python's pyserial, or even a plain terminal /
 * Arduino Serial Monitor for debugging.
 */

#ifndef SERIAL_STREAMER_H
#define SERIAL_STREAMER_H

#include <Arduino.h>

class SerialStreamer {
  public:
    explicit SerialStreamer(HardwareSerial &serial) : _serial(serial) {}

    void begin(unsigned long baud) {
      _serial.begin(baud);
    }

    void sendHeader(int sampleRateHz) {
      _serial.println("# Through-Wall Motion Detection - ESP32 radar streamer");
      _serial.print("# sample_rate_hz=");
      _serial.println(sampleRateHz);
    }

    void sendSample(uint16_t value) {
      _serial.println(value);
    }

  private:
    HardwareSerial &_serial;
};

#endif // SERIAL_STREAMER_H
