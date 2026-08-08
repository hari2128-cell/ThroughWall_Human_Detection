# Literature Review

Background concepts and prior art this project builds on.

## 1. Doppler radar for motion sensing
Continuous-wave (CW) Doppler radar is used widely for contactless detection
of human presence and gross motion. A stationary target reflects the
transmitted wave with no frequency shift; a moving target shifts it by
`f_d = 2 * v * f_c / c`, where `v` is radial velocity, `f_c` the carrier
frequency, and `c` the speed of light. For a ~10.525 GHz X-band module
(typical of low-cost HB100-class sensors), walking-speed targets (~1 m/s)
produce Doppler shifts in the tens-of-Hz range — within reach of an ESP32
ADC + FFT pipeline without specialized RF hardware.

## 2. Through-wall propagation
X-band microwaves (~8-12 GHz) penetrate common non-metallic building
materials (wood, drywall, thin brick, glass) with attenuation depending on
thickness and moisture. Metallic surfaces (foil-backed insulation, metal
studs, rebar-dense concrete) reflect or heavily attenuate the signal — see
`experiments/Different_Walls` for measured behavior.

## 3. Alternatives considered

| Method | Line-of-sight required | Works through walls | Notes |
|---|---|---|---|
| PIR | Yes | No | Blind to non-thermal motion, no wall penetration |
| Ultrasonic | Yes | No | Short range, blocked by any solid obstacle |
| Camera / vision | Yes | No | Fails in darkness, smoke, occlusion |
| CW Doppler radar (this project) | No | Yes (non-metallic) | No range without added modulation |
| FMCW / UWB radar | No | Yes | Adds range resolution, higher cost/complexity |

## 4. Signal processing techniques referenced
- Sliding-window (short-time) FFT for time-varying frequency content
- Butterworth IIR band-pass filtering to isolate ~0.5-40 Hz motion band
- Energy-threshold detection as an interpretable baseline before ML-based
  classification (see Future Improvements)

## 5. Suggested papers to add
Populate with specific papers used in your final report, e.g. search terms:
"through-wall Doppler radar human detection", "CW radar occupancy sensing",
"micro-Doppler human activity classification". Store PDFs under
`docs/Datasheets/` or a new `papers/` subfolder here.
