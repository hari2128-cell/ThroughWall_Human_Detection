# Visualization Scripts

`quick_plot.py` — generates a single static PNG (raw signal, filtered
signal, FFT spectrum) from a recorded CSV. Faster than launching the full
interactive GUI when you just need a figure for a report or slide.

## Usage

```bash
python quick_plot.py \
  --input ../../datasets/Raw/human_walking.csv \
  --output ../../results/Graphs/human_walking_quicklook.png
```

Example output already generated:
`results/Graphs/human_walking_quicklook.png` — shows a clean ~3.5 Hz
Doppler-shift peak from the synthetic walking sample, versus near-zero
energy for the static sample (generate that comparison with
`--input ../../datasets/Raw/static_no_motion.csv`).
