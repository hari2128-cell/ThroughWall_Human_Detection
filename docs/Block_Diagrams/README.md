# Block Diagrams

## Top-level hardware block diagram

```
 ┌────────────────────┐        analog IF signal        ┌──────────────────────┐
 │  Microwave Doppler  │ ──────────────────────────────►│   ESP32 (ADC1_CH6,    │
 │  Radar Module       │                                 │   GPIO34)              │
 │  (e.g. HB100 class) │◄──────────────────────────────  │                        │
 └────────────────────┘        5V / 3.3V + GND           └──────────┬─────────────┘
                                                                     │ USB UART
                                                                     │ 115200 baud
                                                                     ▼
                                                          ┌──────────────────────┐
                                                          │   Host PC              │
                                                          │  MATLAB / Python        │
                                                          │  (filter, FFT,          │
                                                          │   detect, visualize)    │
                                                          └──────────────────────┘
```

## Power block diagram

```
USB 5V (from PC or wall adapter)
       │
       ├──► ESP32 onboard 3.3V LDO ──► ESP32 core, ADC reference
       │
       └──► Radar module VCC (check datasheet: many need 5V for RF
             frontend, separate from the 3.3V logic-level IF output
             the ESP32 reads)
```

See `hardware/Power_Management/README.md` for regulator/decoupling notes.

## Notes
Replace this text version with an exported graphic once finalized, and
reference it here.
