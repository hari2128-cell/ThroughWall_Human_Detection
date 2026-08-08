# Python GUI

`radar_gui.py` — real-time matplotlib dashboard: live waveform, frequency
spectrum, and scrolling motion-intensity heatmap, updated every 250ms.
Functionally mirrors `signal_processing/MATLAB/live_radar_pipeline.m` for
users without a MATLAB license.

## Setup

```bash
pip install -r ../../scripts/requirements.txt
```

## Usage

```bash
python radar_gui.py --port /dev/ttyUSB0 --baud 115200
```
(On Windows, `--port COM3` etc.)

## What you'll see

- **Top panel**: filtered time-domain signal, title changes to
  "MOTION DETECTED" (with energy value) when the threshold is exceeded.
- **Middle panel**: live frequency spectrum (FFT).
- **Bottom panel**: scrolling heatmap of spectral energy over time.

Tune `MOTION_THRESH` at the top of the script to match the value chosen in
`experiments/Accuracy_Evaluation`.
