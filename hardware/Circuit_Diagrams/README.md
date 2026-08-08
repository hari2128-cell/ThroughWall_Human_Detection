# Circuit Diagrams

## Wiring schematic (text form)

```
                     ┌───────────────────────────┐
                     │      ESP32 Dev Board       │
                     │                            │
   Radar IF OUT ─────┤ GPIO34 (ADC1_CH6)          │
                     │                            │
   Radar GND ────────┤ GND                        │
                     │                            │
   Radar VCC ◄───────┤ 5V (VIN) or 3.3V*          │
                     │                            │
                     │      USB ────────────────────────► Host PC (power + UART)
                     └───────────────────────────┘

  * Check your specific radar module's datasheet — many CW Doppler modules
    (e.g. HB100 boards with onboard IF amp) run on 5V; some low-power
    variants accept 3.3V. Do not exceed the module's rated voltage.

  Decoupling: place a 100nF ceramic capacitor across the radar module's
  VCC/GND pins as close to the module as possible, plus a 10uF bulk
  capacitor across the supply rail, to reduce power-supply noise coupling
  into the sensitive IF signal.
```

## Signal path notes

- The radar's IF output is a small-amplitude AC signal riding on a DC bias.
  The firmware's DC-offset removal (mirrored in
  `signal_processing/Noise_Removal/removeDCOffset.m`) strips this bias
  before filtering — no extra analog high-pass circuit is strictly
  required, but adding a simple RC high-pass (e.g. 1µF + 100kΩ, cutoff
  ~1.6 Hz) ahead of the ADC pin improves SNR by rejecting drift before
  digitization. If added, document the exact RC values here.
- Keep radar-to-ESP32 wiring short (< 15 cm) to minimize noise pickup on the
  analog line.

## Files to add
- [ ] Exported schematic (KiCad, Fritzing, or hand-drawn scan) as
      `radar_esp32_schematic.png` / `.pdf`
- [ ] Breadboard layout photo/diagram

This text schematic is the authoritative source until a graphic is added.
