# Experiment: Multiple Moving Targets

## Objective
Observe system behavior when more than one person/moving object is in the
radar's field of view simultaneously, and document the known limitation
that a single-channel CW radar + simple FFT-peak approach cannot cleanly
separate multiple targets.

## Setup
Two subjects move independently within the radar's field of view — e.g.
walking at different speeds, or one static + one moving.

## Procedure
1. Record trials with 1 subject (baseline), then 2 subjects moving
   independently, then 2 subjects at different but overlapping speeds.
2. Use `signal_processing/FFT/shortTimeFFT.m` to generate a spectrogram and
   visually inspect whether distinct peaks/tracks are visible for each
   target, versus a single blended peak.

## Results (fill in with your measurements)

| Scenario | Distinct spectral peaks observed? | Motion detected (binary)? | Notes |
|---|---|---|---|
| 1 subject walking | _fill in_ | _fill in_ | Baseline |
| 2 subjects, same speed | _fill in_ | _fill in_ | Expect single blended peak |
| 2 subjects, different speeds | _fill in_ | _fill in_ | May show 2 peaks if speeds differ enough |
| 1 static + 1 moving | _fill in_ | _fill in_ | Static target contributes ~no Doppler energy |

## Known limitation

The current `detectMotion.m` only answers "is *some* motion present," and
`analyzeDoppler.m` reports only the single dominant peak — with multiple
targets at similar speeds, their reflections blend into one spectral peak
and cannot be individually resolved. Separating and counting simultaneous
targets would need either an FMCW radar (adds range-gating) or a phased/
multi-antenna array (adds angle-of-arrival) — see Future Improvements in
the top-level README.
