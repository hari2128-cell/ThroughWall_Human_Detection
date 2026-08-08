# Performance Report

Summary of measured system performance. Source data and reproduction steps
are in `experiments/`; this document is the consolidated "final numbers"
view for reports/interviews/presentations.

## Detection accuracy (synthetic labeled dataset)

From `experiments/Accuracy_Evaluation/README.md` — full methodology and
reproduction steps there.

| Metric | Value |
|---|---|
| Precision | 1.00 |
| Recall | 1.00 |
| F1 score | 1.00 |
| Chosen threshold | ≈ 62.6 (energy units) |

⚠️ Computed on the **synthetic** example dataset shipped in
`datasets/Labeled/` — demonstrates the evaluation pipeline works
end-to-end. Replace with numbers from your own recorded hardware data
before citing as real-world performance (see the same warning in
`experiments/Accuracy_Evaluation/README.md`).

## Signal quality comparison

| Recording | Band-limited energy (0.5-40Hz) |
|---|---|
| `static_no_motion.csv` | 2.74 |
| `human_walking.csv` | 8482.92 |

~3000x separation between static and motion energy in this synthetic
example — see `results/Graphs/static_no_motion_quicklook.png` vs.
`results/Graphs/human_walking_quicklook.png` for the visual comparison, and
`results/Heatmaps/` for the corresponding spectrograms.

## Latency

| Stage | Approx. time |
|---|---|
| Analysis window | 2 s |
| Update hop | 0.25 s |
| End-to-end detection latency | < 0.5 s (dominated by window length, not compute) |

## Range / material performance

Not yet measured on real hardware — see `experiments/Distance_Test` and
`experiments/Different_Walls` for the test procedures and result tables to
fill in once hardware trials are run.

## Known limitations (see relevant subfolder READMEs for detail)
- No target range estimation (CW radar, not FMCW)
- No approach/recede direction (needs I/Q front-end)
- Single blended peak with multiple simultaneous targets
  (`experiments/Multi_Target`)
- Detection threshold is hardware- and environment-specific and must be
  re-tuned per deployment
