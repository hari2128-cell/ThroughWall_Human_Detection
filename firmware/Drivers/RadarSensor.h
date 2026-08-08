/*
 * RadarSensor.h
 * Minimal driver wrapping ESP32 ADC configuration and reads for the
 * microwave Doppler radar's analog IF output.
 *
 * This mirrors the sampling logic in main/main.ino but as a reusable
 * class, useful if you split the sketch into multiple files or write
 * unit tests against it (see firmware/Tests).
 */

#ifndef RADAR_SENSOR_H
#define RADAR_SENSOR_H

#include <Arduino.h>

class RadarSensor {
  public:
    RadarSensor(uint8_t adcPin, adc_attenuation_t atten = ADC_11db, uint8_t resolutionBits = 12)
      : _pin(adcPin), _atten(atten), _resolutionBits(resolutionBits) {}

    void begin() {
      analogReadResolution(_resolutionBits);
      analogSetPinAttenuation(_pin, _atten);
    }

    // Returns the raw ADC sample (0 .. 2^resolutionBits - 1)
    uint16_t readRaw() {
      return analogRead(_pin);
    }

    // Returns the sample converted to volts, assuming ~3.3V full scale
    // with 11dB attenuation. Adjust REF_VOLTAGE if using a different
    // attenuation setting.
    float readVolts() {
      const float REF_VOLTAGE = 3.3f;
      uint16_t raw = readRaw();
      uint16_t maxCount = (1 << _resolutionBits) - 1;
      return (raw / (float)maxCount) * REF_VOLTAGE;
    }

  private:
    uint8_t _pin;
    adc_attenuation_t _atten;
    uint8_t _resolutionBits;
};

#endif // RADAR_SENSOR_H
