# Experiment: Different Wall Materials

## Objective
Characterize how much the radar's ability to detect motion degrades when
sensing through various common building materials, and identify materials
that block detection entirely (e.g. metal-backed surfaces).

## Setup
Fix the radar-to-subject distance (e.g. 2m) and repeat the `Human_Motion`
walking test through each material below, keeping subject speed and path
consistent across trials.

## Materials to test

| Material | Thickness | Detected? | Peak energy (relative to open-LOS baseline) | Notes |
|---|---|---|---|---|
| None (open line-of-sight, baseline) | — | Yes | 100% | Reference |
| Wooden door | ~35mm | _fill in_ | _fill in_ | |
| Drywall (single layer) | ~12mm | _fill in_ | _fill in_ | |
| Drywall (double layer / wall cavity) | ~24mm+ | _fill in_ | _fill in_ | |
| Glass window | ~4-6mm | _fill in_ | _fill in_ | |
| Thin brick wall | ~100mm | _fill in_ | _fill in_ | |
| Metal door / foil-backed insulation | — | _fill in (expect blocked)_ | _fill in_ | Expected to heavily attenuate or block — X-band microwaves reflect off metal |

## Procedure
1. Record a baseline (no wall) human-motion trial.
2. For each material, record 3 trials of the same walking pattern through
   the material at the same distance.
3. Compute band energy for each trial via `analyze_recording.m` and express
   as a percentage of the baseline's mean energy.

## Expected outcome
Energy should decrease with material density/thickness, with a sharp
drop-off for any metallic material — this matches the working principle
described in `docs/Problem_Statement.md` (non-metallic obstacles only).
Document your actual measured attenuation trend here once data is
collected, and re-tune `motionThresh` per-material if deploying against a
specific wall type.
