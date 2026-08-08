# Flowcharts

Text/ASCII versions of the system flowcharts — the source of truth for
content. Export polished versions (draw.io, PowerPoint) into this folder as
`.png`/`.pdf` when ready.

## 1. Firmware loop

```
        ┌─────────────────────┐
        │ Setup: init ADC,     │
        │ Serial, timers       │
        └──────────┬───────────┘
                   ▼
        ┌─────────────────────┐
 ┌─────►│ Time to sample?      │
 │      │ (elapsed >= period)  │
 │      └──────────┬───────────┘
 │             yes │  no
 │                 ▼      └──────┐
 │      ┌─────────────────────┐  │
 │      │ analogRead(GPIO34)   │  │
 │      └──────────┬───────────┘  │
 │                 ▼               │
 │      ┌─────────────────────┐   │
 │      │ Push sample to        │   │
 │      │ ring buffer           │   │
 │      └──────────┬───────────┘   │
 │                 ▼               │
 │      ┌─────────────────────┐   │
 │      │ Drain buffer to        │◄──┘
 │      │ Serial (println)       │
 │      └──────────┬───────────┘
 │                 │
 └─────────────────┘
```

## 2. End-to-end signal processing pipeline

```
Raw ADC samples
     │
     ▼
Remove DC offset  ───────────────►  signal_processing/Noise_Removal
     │
     ▼
Band-pass filter (0.5-40 Hz)  ──►  signal_processing/Filtering
     │
     ▼
Windowed FFT  ───────────────────► signal_processing/FFT
     │
     ▼
Doppler shift interpretation  ───► signal_processing/Doppler_Analysis
     │
     ▼
Feature extraction  ─────────────► signal_processing/Feature_Extraction
     │
     ▼
Threshold classification  ───────► signal_processing/Motion_Detection
     │
     ▼
Visualization  ───────────────────► visualization/
```

## 3. Motion decision logic

```
        ┌───────────────────────┐
        │ Compute band energy E  │
        └───────────┬─────────────┘
                    ▼
        ┌───────────────────────┐
        │ E > threshold?         │
        └─────┬─────────────┬────┘
           yes│              │no
              ▼              ▼
     ┌────────────────┐  ┌────────────────┐
     │ MOTION DETECTED │  │   NO MOTION     │
     └────────────────┘  └────────────────┘
```
