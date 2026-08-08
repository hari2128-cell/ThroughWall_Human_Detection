# Live Monitoring

Real-time monitoring options beyond the full matplotlib GUI in
`visualization/Python_GUI`:

## `terminal_dashboard.py`

A headless-friendly, text-only live monitor — prints a scrolling status
line (`MOTION DETECTED` / `no motion`) with a live energy bar to the
terminal. Useful when:
- Running on a Raspberry Pi / SSH session without a display
- Running as a background/systemd service where you just want a log/status
  line, not a plot window

```bash
python terminal_dashboard.py --port /dev/ttyUSB0 --threshold 3.0
```

## Other live options in this repo

| Tool | Where | Best for |
|---|---|---|
| `signal_processing/MATLAB/live_radar_pipeline.m` | MATLAB | Full waveform + spectrum + heatmap, MATLAB users |
| `visualization/Python_GUI/radar_gui.py` | Python | Same, for non-MATLAB users, matplotlib GUI |
| `terminal_dashboard.py` (this folder) | Python | Headless/SSH, minimal dependencies at runtime |
| `visualization/Serial_Plotter` | Arduino IDE | Zero-setup quick check straight from the IDE |
