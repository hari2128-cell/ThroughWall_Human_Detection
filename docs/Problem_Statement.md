# Problem Statement

Design a low-cost embedded system capable of detecting human movement behind
non-metallic obstacles using Doppler radar, while minimizing false detections
caused by environmental noise.

## Requirements

The system should:

1. Acquire radar signals continuously via ESP32 ADC.
2. Filter unwanted noise (electrical, environmental, DC offset).
3. Detect motion using frequency/energy features extracted via FFT.
4. Visualize signal characteristics in real time (waveform, spectrum, heatmap).
5. Operate with low latency suitable for live monitoring.

## Working principle (Doppler Effect)

The radar continuously transmits microwave signals.

- Stationary objects reflect waves with nearly identical frequency.
- Moving objects reflect waves with a slightly shifted frequency (the Doppler
  frequency).

This shift is converted by the radar module into an analog electrical signal
carrying information about movement, velocity, direction, and motion intensity.
The ESP32 captures this signal for processing.

## Engineering challenges

- Maintaining a constant sampling frequency
- Removing environmental noise
- Selecting a suitable detection threshold
- Reducing false positives
- Obtaining stable analog signals
- Synchronizing MATLAB with serial communication
- Visualizing real-time data efficiently
