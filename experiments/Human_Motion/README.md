# Experiment: Human Motion (Primary Detection Test)

## Objective
Verify the system correctly detects a person walking/moving within the
radar's field of view, in open line-of-sight (baseline, before adding a
wall — see `Different_Walls` for the through-wall variant).

## Setup
- Radar module in open line-of-sight to the test subject.
- Subject walks back and forth, or performs gestures, at a known
  approximate distance (e.g. 1m, 2m, 3m).

## Procedure
1. Record a static baseline first (see `Static_Object`) for comparison.
2. `python scripts/Data_Collection/record_serial_to_csv.py --port <PORT> --duration 30 --out datasets/Raw/human_motion_1m.csv`
3. Repeat at each test distance.
4. Analyze each with `analyze_recording.m`; note the dominant Doppler peak
   frequency and estimated speed from `Doppler_Analysis/analyzeDoppler.m`.

## Results (fill in with your measurements)

| Distance | Motion type | Peak freq (Hz) | Est. speed (m/s) | Detected? |
|---|---|---|---|---|
| 1 m | Walking | _fill in_ | _fill in_ | _fill in_ |
| 2 m | Walking | _fill in_ | _fill in_ | _fill in_ |
| 3 m | Walking | _fill in_ | _fill in_ | _fill in_ |
| 1 m | Arm wave | _fill in_ | _fill in_ | _fill in_ |

## Notes / observations
Record qualitative observations here: detection latency, effect of walking
speed/direction, any missed detections and likely cause.
