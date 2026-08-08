# Doppler Analysis

Converts a frequency-domain spectrum into physically meaningful motion
information.

## `analyzeDoppler.m`

Given an FFT spectrum, finds the dominant peak and converts it to an
estimated radial speed using the Doppler equation:

```
f_d = 2 * v * f_c / c
```

- `f_d` — measured Doppler shift (Hz)
- `v`   — target radial velocity (m/s)
- `f_c` — radar carrier frequency (Hz)
- `c`   — speed of light

Rearranged to solve for speed: `v = f_d * c / (2 * f_c)`.

## Limitations of this single-channel setup

- **No direction (toward/away)**: distinguishing approach from recession
  needs an I/Q (quadrature) demodulator front-end; most low-cost CW modules
  used here only provide a single real-valued IF output.
- **No range**: this is a CW (not FMCW) radar, so it reports *that* and
  *how fast* something is moving, not *how far away*. Range estimation would
  require frequency modulation and beat-frequency analysis — see Future
  Improvements in the top-level README.
- **Single-target assumption**: with multiple moving targets, the FFT peak
  reflects whichever produces the strongest reflection; see
  `experiments/Multi_Target` for observed behavior in that case.
