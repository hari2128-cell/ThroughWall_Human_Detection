# Visualization

Multiple ways to view radar data, from a zero-setup hardware sanity check
up to full real-time analysis:

| Folder | Tool | Setup required |
|---|---|---|
| `Serial_Plotter/` | Arduino IDE built-in plotter | None — just flash the firmware |
| `Live_Monitoring/` | Python terminal dashboard | Python + pyserial/numpy/scipy |
| `Python_GUI/` | Python + matplotlib live GUI (waveform/spectrum/heatmap) | Python + matplotlib/pyserial/scipy |
| `Heatmaps/` | Offline heatmap generator (PNG output) | Python + matplotlib/scipy |
| (MATLAB equivalent) | `signal_processing/MATLAB/live_radar_pipeline.m` | MATLAB |

Start with `Serial_Plotter` to confirm hardware is working, then move to
`Python_GUI` or the MATLAB pipeline for real filtering/FFT/detection.
