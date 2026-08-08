# Signal Processing

Modular DSP pipeline, one folder per stage, each independently usable and
testable:

```
Data_Acquisition → Noise_Removal → Filtering → FFT → Doppler_Analysis
                                                   ↘
                                              Feature_Extraction → Motion_Detection
```

| Folder | Stage |
|---|---|
| `Data_Acquisition/` | Read raw samples from serial |
| `Noise_Removal/` | DC offset removal, moving-average smoothing |
| `Filtering/` | Butterworth low/high/band-pass filtering |
| `FFT/` | Windowed FFT and sliding-window spectrogram |
| `Doppler_Analysis/` | Convert frequency shift to estimated speed |
| `Feature_Extraction/` | Reduce spectrum to a small feature vector |
| `Motion_Detection/` | Threshold-based classification + threshold tuning |
| `MATLAB/` | End-to-end scripts (`live_radar_pipeline.m`, `analyze_recording.m`) that wire the above together |

See each subfolder's README for function-level documentation.
