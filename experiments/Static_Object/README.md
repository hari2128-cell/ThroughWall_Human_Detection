# Experiment: Static Object (Baseline / False-Positive Check)

## Objective
Confirm the system reports "no motion" when nothing is moving, and
characterize the noise floor (baseline spectral energy) used to set the
detection threshold in `signal_processing/Motion_Detection`.

## Setup
- Radar module powered on, aimed at an empty room / static scene
  (furniture, walls — nothing moving, including no fans, curtains, or
  pets in the field of view).
- Recorded via `scripts/Data_Collection/record_serial_to_csv.py`, 30-60s
  captures, saved to `datasets/Raw/` (or `datasets/Labeled/` as
  `static_XX.csv` for threshold tuning).

## Procedure
1. `python scripts/Data_Collection/record_serial_to_csv.py --port <PORT> --duration 60 --out datasets/Raw/static_baseline.csv`
2. Analyze with `signal_processing/MATLAB/analyze_recording.m` or
   `visualization/Python_GUI/radar_gui.py`.
3. Record the observed spectral energy range below.

## Results (fill in with your measurements)

| Trial | Duration | Mean energy | Max energy | False positives (energy > threshold) |
|---|---|---|---|---|
| 1 | 60s | _fill in_ | _fill in_ | _fill in_ |
| 2 | 60s | _fill in_ | _fill in_ | _fill in_ |

## Notes / observations
- Document any environmental sources of false positives observed (e.g. HVAC
  vibration, fluorescent light flicker, Wi-Fi/BLE interference) here.
- The `motionThresh` value in `live_radar_pipeline.m` / `detectMotion.m`
  should sit comfortably above the maximum static-scene energy observed
  here — see `experiments/Accuracy_Evaluation` for the formal sweep.
