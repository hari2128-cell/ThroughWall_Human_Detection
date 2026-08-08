# Power Management

## Supply architecture

The system runs entirely from a single USB 5V source (PC port or USB power
adapter):

```
USB 5V
  ├──► ESP32 onboard 3.3V LDO regulator ──► ESP32 core, ADC reference
  └──► Radar module VCC (5V or 3.3V per its datasheet)
```

## Current budget (approximate)

| Load | Typical current | Notes |
|---|---|---|
| ESP32 (Wi-Fi off, active) | ~80-160 mA | Reduce further with `WiFi.mode(WIFI_OFF)` if unused |
| ESP32 ADC + UART streaming | negligible extra | Small vs. core draw |
| Radar module | ~10-40 mA | Check exact module datasheet |
| **Total** | **~100-200 mA** | Well within standard USB port budget (500 mA+) |

## Noise / decoupling recommendations

1. Place a 100nF ceramic capacitor directly across the radar module's
   VCC/GND pins.
2. Add a 10µF bulk capacitor across the shared supply rail near the radar
   module to smooth transients from ESP32 CPU/Wi-Fi activity, which can
   couple into the sensitive analog IF line as periodic noise spikes.
3. If powering from a noisy USB hub or long cable, consider a dedicated
   linear regulator (AMS1117-3.3/5.0) for the radar module rather than
   sharing the ESP32's onboard regulator.

## Future improvement: battery operation

For a portable/wireless version, a LiPo battery + TP4056 charge module +
boost/buck regulator would replace the USB supply. Document battery
capacity vs. expected runtime here once implemented.
