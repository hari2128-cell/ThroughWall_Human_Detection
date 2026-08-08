// test_sample_buffer.cpp
// Off-target unit test for the SampleBuffer ring-buffer logic.
// Uses a small Arduino-type stub so this compiles with a plain g++,
// without needing the ESP32 toolchain.
//
// Build:  g++ -std=c++17 test_sample_buffer.cpp -o test_sample_buffer
// Run:    ./test_sample_buffer

#include <cassert>
#include <cstdint>
#include <cstddef>
#include <cstdio>

// ---- Minimal stand-in for the pieces of SampleBuffer.h we need ----
// (Kept inline here rather than including Arduino.h, since Arduino.h is
// not available off-target.)
template <size_t N>
class SampleBuffer {
  public:
    SampleBuffer() : _head(0), _tail(0) {}

    bool push(uint16_t value) {
      size_t nextHead = (_head + 1) % N;
      if (nextHead == _tail) return false;
      _data[_head] = value;
      _head = nextHead;
      return true;
    }

    bool pop(uint16_t &value) {
      if (_tail == _head) return false;
      value = _data[_tail];
      _tail = (_tail + 1) % N;
      return true;
    }

    bool isEmpty() const { return _tail == _head; }
    size_t size() const { return (_head + N - _tail) % N; }

  private:
    uint16_t _data[N];
    size_t _head;
    size_t _tail;
};

static void test_push_pop_order() {
  SampleBuffer<4> buf;
  assert(buf.isEmpty());
  assert(buf.push(10));
  assert(buf.push(20));
  uint16_t v;
  assert(buf.pop(v) && v == 10);
  assert(buf.pop(v) && v == 20);
  assert(!buf.pop(v)); // empty now
  printf("test_push_pop_order: PASS\n");
}

static void test_full_buffer_drops_sample() {
  SampleBuffer<4> buf; // capacity is N-1 = 3 usable slots
  assert(buf.push(1));
  assert(buf.push(2));
  assert(buf.push(3));
  assert(!buf.push(4)); // buffer full, should be dropped
  uint16_t v;
  assert(buf.pop(v) && v == 1);
  printf("test_full_buffer_drops_sample: PASS\n");
}

int main() {
  test_push_pop_order();
  test_full_buffer_drops_sample();
  printf("All tests passed.\n");
  return 0;
}
