# Datasets

| Folder | Contents |
|---|---|
| `Raw/` | Unprocessed serial captures straight from `scripts/Data_Collection/record_serial_to_csv.py` (one `adc_sample` column) |
| `Processed/` | Filtered/cleaned versions of `Raw/` recordings (after DC removal + band-pass), produced by `scripts/Data_Preprocessing` |
| `Labeled/` | Recordings with known ground truth for tuning/evaluating the detector — filenames prefixed `static_*` or `motion_*`. Populated here with **synthetic example data** (5 static + 5 motion, 4s each @ 1kHz) so `signal_processing/Motion_Detection/tuneThreshold.m` and `experiments/Accuracy_Evaluation` are runnable out of the box. **Replace with your own real recordings** once you have hardware. |
| `Sample_Recordings/` | Two representative example recordings (`static_no_motion.csv`, `human_walking.csv`, 10s @ 1kHz, synthetic) used in `docs/`, `experiments/`, and quick demos of `analyze_recording.m` |

## ⚠️ Synthetic data notice

The CSV files currently in `Labeled/` and `Sample_Recordings/` are
**synthetically generated** (sine-wave-modulated signal + noise standing in
for a walking-speed Doppler return) so the repository is runnable and every
script has real input to demonstrate against. They are **not** real radar
captures. Swap them out for your own hardware recordings before citing any
numeric results (accuracy, thresholds) in a report or interview — see
`experiments/Accuracy_Evaluation/README.md` for the labeling convention to
follow when you do.

## CSV format

Single column, header `adc_sample`, one 12-bit ADC value (0-4095) per row,
sampled at 1000 Hz (matches `firmware/ESP32/main/main.ino`).
