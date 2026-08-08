# Filtering

| Function | Purpose |
|---|---|
| `bandpassFilterSignal.m` | Combined 0.5-40 Hz band-pass — the default filter used in the live pipeline |
| `lowpassFilterSignal.m` | Standalone low-pass (reject high-frequency noise) |
| `highpassFilterSignal.m` | Standalone high-pass (reject DC/slow drift) |

All filters are 4th-order Butterworth, applied zero-phase via `filtfilt` so
motion-event timing in the output is not shifted relative to the input —
important since later stages (`Doppler_Analysis`, `Motion_Detection`)
reason about *when* energy appears, not just its frequency content.

## Choosing cutoff frequencies

- **Lower cutoff (~0.5 Hz)**: rejects DC offset/slow thermal or mechanical
  drift while still passing very slow motion.
- **Upper cutoff (~40 Hz)**: covers Doppler shifts from typical human
  walking/gesturing speeds at X-band (~10 GHz) radar frequency; raise this
  if you need to capture faster motion (e.g. running) or lower it to reject
  more high-frequency electrical noise at the cost of missing fast motion.

Re-tune these in `experiments/` against your specific radar module and
target speeds — see `experiments/Accuracy_Evaluation`.
