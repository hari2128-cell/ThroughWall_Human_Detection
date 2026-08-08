/*
 * Through-Wall Human Motion Detection
 * ESP32 firmware: samples the microwave Doppler radar's analog IF output
 * and streams the samples over USB serial to MATLAB / Python for
 * filtering, FFT, and motion detection.
 *
 * Wiring:
 *   Radar IF/analog output -> ESP32 GPIO34 (ADC1_CH6)
 *   Radar VCC              -> 5V or 3.3V per module datasheet
 *   Radar GND              -> GND
 *
 * Protocol:
 *   One unsigned integer ADC sample (0-4095) per line, newline terminated,
 *   at SAMPLE_RATE_HZ samples/sec, over serial at BAUD_RATE.
 */

#include <Arduino.h>

// ---------- Configuration ----------
static const int   RADAR_ADC_PIN   = 34;      // ADC1 channel, input-only pin
static const int   BAUD_RATE       = 115200;
static const int   SAMPLE_RATE_HZ  = 1000;    // sampling frequency
static const int   ADC_RESOLUTION  = 12;      // bits (0-4095)
static const unsigned long SAMPLE_PERIOD_US = 1000000UL / SAMPLE_RATE_HZ;

// Simple ring buffer to decouple sampling timing from serial writes
static const int BUFFER_SIZE = 64;
static uint16_t sampleBuffer[BUFFER_SIZE];
static volatile int bufHead = 0;
static volatile int bufTail = 0;

unsigned long lastSampleMicros = 0;

void setup() {
  Serial.begin(BAUD_RATE);
  analogReadResolution(ADC_RESOLUTION);
  analogSetPinAttenuation(RADAR_ADC_PIN, ADC_11db); // full 0-3.3V range

  // Let serial settle
  delay(200);
  Serial.println("# Through-Wall Motion Detection - ESP32 radar streamer");
  Serial.print("# sample_rate_hz=");
  Serial.println(SAMPLE_RATE_HZ);

  lastSampleMicros = micros();
}

void loop() {
  unsigned long now = micros();

  // Sample at a fixed rate
  if (now - lastSampleMicros >= SAMPLE_PERIOD_US) {
    lastSampleMicros += SAMPLE_PERIOD_US;

    uint16_t value = analogRead(RADAR_ADC_PIN);

    int nextHead = (bufHead + 1) % BUFFER_SIZE;
    if (nextHead != bufTail) { // buffer not full
      sampleBuffer[bufHead] = value;
      bufHead = nextHead;
    }
    // if full, drop the sample (backpressure) rather than blocking timing
  }

  // Drain buffer to serial as fast as possible
  while (bufTail != bufHead) {
    Serial.println(sampleBuffer[bufTail]);
    bufTail = (bufTail + 1) % BUFFER_SIZE;
  }
}
