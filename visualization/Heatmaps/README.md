# Heatmaps

`generate_heatmap.py` — offline heatmap/spectrogram generator. Reads a
recorded CSV, band-pass filters it, computes a sliding-window FFT
(2s window, 0.25s hop by default), and saves a PNG.

## Usage

```bash
python generate_heatmap.py \
  --input ../../datasets/Sample_Recordings/human_walking.csv \
  --output ../../results/Heatmaps/human_walking_heatmap.png
```

Example output already generated from the shipped sample recordings:
`results/Heatmaps/human_walking_heatmap.png` and
`results/Heatmaps/static_no_motion_heatmap.png` — compare the two to see
the difference between a static scene (near-zero energy throughout) and a
walking target (concentrated low-frequency energy band).

For live (real-time, not offline) heatmap rendering, see
`visualization/Live_Monitoring` and `visualization/Python_GUI/radar_gui.py`,
or MATLAB's `signal_processing/MATLAB/live_radar_pipeline.m`.
