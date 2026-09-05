/*
 * SampleBuffer.h
 * Fixed-size ring buffer for decoupling fixed-rate ADC sampling from
 * variable-rate UART transmission. Used by the sensor-interface layer
 * that sits between the low-level RadarSensor driver and the
 * Communication layer.
 */

#ifndef SAMPLE_BUF_H
#define SAMPLE_BUFFER_H

#include <Arduino.h>

template <size_t N>
class SampleBuffer {
  public:
    SampleBuffer() : _head(0), _tail(0) {}

    bool push(uint16_t value) {
      size_t nextHead = (_head + 1) % N;
      if (nextHead == _tail) {
        return false; // buffer full, sample dropped
      }
      _data[_head] = value;
      _head = nextHead;
      return true;
    }

    bool pop(uint16_t &value) {
      if (_tail == _head) {
        return false; // empty
      }
      value = _data[_tail];
      _tail = (_tail + 1) % N;
      return true;
    }

    bool isEmpty() const { return _tail == _head; }
    size_t size() const { return (_head + N - _tail) % N; }

  private:
    uint16_t _data[N];
    volatile size_t _head;
    volatile size_t _tail;
};

#endif // SAMPLE_BUFFER_H
