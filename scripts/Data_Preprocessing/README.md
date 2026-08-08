# Data Preprocessing

`preprocess_recording.py` — batch-applies DC-offset removal + 0.5-40 Hz
Butterworth band-pass filtering to every CSV in `datasets/Raw/`, saving
cleaned versions into `datasets/Processed/`. This is the same filtering
step applied live in the real-time pipelines, so processed files reflect
exactly what the detector "sees" and are convenient for offline plotting,
threshold tuning, or feeding into `visualization/Heatmaps`.

## Usage

```bash
python preprocess_recording.py \
  --input-dir ../../datasets/Raw \
  --output-dir ../../datasets/Processed
```

Already run once against the shipped sample recordings — see
`datasets/Processed/human_walking.csv` and
`datasets/Processed/static_no_motion.csv` for example output.
