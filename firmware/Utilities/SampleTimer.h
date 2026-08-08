/*
 * SampleTimer.h
 * Fixed-rate scheduling helper so the main loop can poll "is it time to
 * sample yet?" without blocking (no delay()), keeping UART draining
 * responsive between samples.
 */

#ifndef SAMPLE_TIMER_H
#define SAMPLE_TIMER_H

#include <Arduino.h>

class SampleTimer {
  public:
    explicit SampleTimer(unsigned long periodMicros)
      : _periodMicros(periodMicros), _lastMicros(0) {}

    void begin() {
      _lastMicros = micros();
    }

    // Returns true (and advances the schedule) if a new sample is due.
    bool isDue() {
      unsigned long now = micros();
      if (now - _lastMicros >= _periodMicros) {
        _lastMicros += _periodMicros;
        return true;
      }
      return false;
    }

    void setRateHz(int hz) {
      _periodMicros = 1000000UL / (unsigned long)hz;
    }

  private:
    unsigned long _periodMicros;
    unsigned long _lastMicros;
};

#endif // SAMPLE_TIMER_H
