# Noise Removal

| Function | Purpose |
|---|---|
| `removeDCOffset.m` | Subtracts the signal mean to eliminate the radar IF's DC bias |
| `movingAverageFilter.m` | Optional lightweight smoothing (alternative/supplement to Butterworth filtering in `signal_processing/Filtering`) |

## Noise sources addressed

- **Electrical interference** — mains hum, switching-regulator noise —
  attenuated by the band-pass filter in `signal_processing/Filtering`
  (rejects everything outside ~0.5-40 Hz).
- **DC offset** — removed here via `removeDCOffset.m`.
- **ADC quantization noise** — inherent to 12-bit sampling; averaged out by
  the FFT's windowing/integration over many samples.
- **Environmental vibration / EMI** — mitigated by physical setup (short
  wiring, decoupling capacitors — see `hardware/Power_Management`) rather
  than software alone.
