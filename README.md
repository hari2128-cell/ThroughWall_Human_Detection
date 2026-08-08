# Through-Wall Human Motion Detection using Microwave Doppler Radar and ESP32

An embedded sensing system that detects human presence and motion behind non-metallic
obstacles (wooden doors, drywall, thin brick) using a microwave Doppler radar sensor,
an ESP32 microcontroller, and MATLAB-based digital signal processing.

## Why this project

Cameras, PIR, and ultrasonic sensors all need a direct line of sight. Microwave
Doppler radar does not — it transmits electromagnetic waves that pass through many
common building materials and analyzes the reflected signal for the frequency shift
caused by a moving body (the Doppler effect).

Applications: search & rescue, security/intruder detection, smart-home occupancy
sensing, contactless monitoring.

## System architecture

```
Human Motion
     │
     ▼
Microwave Doppler Radar  ──►  Analog Signal
     │
     ▼
ESP32 ADC  ──►  Digital Samples
     │
     ▼
UART (USB Serial)
     │
     ▼
MATLAB: Filtering → FFT → Motion Detection → Heatmap / Graphs
```

## Repository layout

| Folder | Contents |
|---|---|
| `docs/` | Project overview, problem statement, architecture, literature review, diagrams |
| `hardware/` | BOM, circuit diagrams, PCB, enclosure, power management |
| `firmware/ESP32/` | Arduino/PlatformIO firmware: ADC sampling + UART streaming |
| `signal_processing/MATLAB/` | Acquisition, filtering, FFT, Doppler analysis, motion detection |
| `visualization/` | Real-time plotting, heatmaps, Python GUI, serial plotter |
| `datasets/` | Raw / processed / labeled radar recordings |
| `experiments/` | Test logs: static object, human motion, wall types, distance, multi-target |
| `scripts/` | Data collection, preprocessing, and utility scripts |
| `results/` | Screenshots, heatmaps, graphs, performance reports |
| `presentations/`, `publications/` | Slides, posters, paper drafts |

## Quick start

### 1. Hardware
- ESP32 dev board
- Microwave Doppler radar module (e.g. HB100 + IF amplifier, or CDM324/RCWL-0516 class module with raw IF output)
- Connect the radar's analog IF output to an ESP32 ADC-capable GPIO (default: **GPIO34**)
- Power radar per its datasheet (see `hardware/BOM/`)

### 2. Firmware
Open `firmware/ESP32/main/main.ino` in Arduino IDE (or use PlatformIO with
`firmware/ESP32/platformio.ini`), select your ESP32 board, and upload.
The firmware samples the radar's analog output and streams samples over
USB serial at 115200 baud, one value per line.

### 3. Signal processing / visualization
In MATLAB, open `signal_processing/MATLAB/live_radar_pipeline.m`, set the
correct serial port, and run. It will:
1. Read live samples over serial
2. Remove DC offset and apply a band-pass filter
3. Compute a sliding-window FFT
4. Apply threshold-based motion detection
5. Plot the live waveform, spectrum, and a scrolling motion heatmap

## Documentation

See `docs/Project_Overview.md` and `docs/Problem_Statement.md` for the full
write-up (motivation, working principle, engineering challenges, results,
and future work), and `docs/References/` for background reading on Doppler
radar sensing.

## License

See `LICENSE`.
