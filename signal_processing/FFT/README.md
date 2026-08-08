# FFT

| Function | Purpose |
|---|---|
| `computeFFT.m` | Single-window Hann-windowed FFT magnitude spectrum |
| `shortTimeFFT.m` | Sliding-window FFT (spectrogram) across a full recording — feeds heatmap generation |

## Why windowing matters

A rectangular (unwindowed) FFT of a finite segment introduces spectral
leakage — energy from a true frequency component spreads into neighboring
bins, which can bury a weak Doppler peak in noise. Both functions here apply
a Hann window before transforming to reduce this effect at the cost of
slightly widening the main lobe — an acceptable trade-off for this
application's frequency resolution needs.

## Frequency resolution

Frequency resolution = `Fs / N` where `N` is the window length in samples.
At `Fs = 1000 Hz` and a 2-second window (`N = 2000`), resolution is 0.5 Hz —
sufficient to distinguish walking-speed Doppler shifts from noise floor.
Shortening the window (for lower latency) trades away frequency resolution;
see `experiments/Accuracy_Evaluation` for the latency/resolution trade-off
actually measured on this system.
