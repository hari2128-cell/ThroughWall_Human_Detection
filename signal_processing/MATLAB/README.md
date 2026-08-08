# MATLAB — Integrated Pipelines

This folder contains the two runnable, end-to-end entry points. The
individual processing stages they call live in the sibling folders
(`Data_Acquisition`, `Noise_Removal`, `Filtering`, `FFT`,
`Doppler_Analysis`, `Feature_Extraction`, `Motion_Detection`) as standalone,
independently testable functions — this folder just wires them together.

| Script | Purpose |
|---|---|
| `live_radar_pipeline.m` | Real-time: read from serial → filter → FFT → detect → plot |
| `analyze_recording.m` | Offline: analyze a previously recorded CSV file |

Add these sibling folders to your MATLAB path before running (or run from
the repo root with `addpath(genpath('signal_processing'))`):

```matlab
addpath(genpath('signal_processing'));
live_radar_pipeline
```
