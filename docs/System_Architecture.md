# System Architecture

```
Human Motion
      │
      ▼
Microwave Doppler Radar
      │
Analog Signal
      │
      ▼
ESP32 ADC
      │
Digital Samples
      │
      ▼
Serial Communication (USB UART)
      │
      ▼
MATLAB
      │
Signal Processing
      │
Filtering
      │
FFT
      │
Motion Detection
      │
Heatmap / Graph
```

## Component responsibilities

| Stage | Component | Responsibility |
|---|---|---|
| Sensing | Microwave Doppler radar | Emit microwaves, reflect off moving targets, output analog IF signal |
| Acquisition | ESP32 (12-bit ADC) | Sample analog signal at fixed rate, buffer, stream via UART |
| Transport | USB UART | Reliable real-time link between ESP32 and host PC |
| Processing | MATLAB | DC removal, band-pass filtering, FFT, threshold-based motion detection |
| Visualization | MATLAB / Python | Waveform, spectrum, and heatmap plots |

Place a rendered architecture diagram (e.g. exported from draw.io or PowerPoint)
at `docs/System_Architecture.pdf` or `docs/Block_Diagrams/` if you want a
polished graphic alongside this text version.
