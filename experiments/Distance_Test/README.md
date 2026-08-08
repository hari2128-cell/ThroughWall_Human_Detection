# Experiment: Detection Range / Distance Test

## Objective
Find the maximum distance at which the system reliably detects human
motion, in open line-of-sight, to characterize sensing range before
combining with a wall (see `Different_Walls`).

## Setup
Subject walks a consistent pattern at increasing distances from the radar,
starting close and stepping back in fixed increments (e.g. 1m steps) until
detection becomes unreliable.

## Procedure
1. At each distance, record 3x 15s trials of the subject walking within
   the radar's field of view.
2. Run `analyze_recording.m` on each; note whether `detectMotion.m` returns
   `true` for at least 2 of the 3 trials at the tuned threshold from
   `experiments/Accuracy_Evaluation`.

## Results (fill in with your measurements)

| Distance | Trial 1 detected? | Trial 2 detected? | Trial 3 detected? | Reliable? |
|---|---|---|---|---|
| 1 m | | | | |
| 2 m | | | | |
| 3 m | | | | |
| 4 m | | | | |
| 5 m | | | | |

## Notes
- Effective range depends heavily on the specific radar module's transmit
  power and antenna gain — document the exact module used
  (`docs/Datasheets/`) alongside these results, since they are not
  transferable across different radar hardware.
- Range typically decreases further once a wall is added (see
  `Different_Walls`); consider repeating this sweep through your primary
  wall material of interest.
