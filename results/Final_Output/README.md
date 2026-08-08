# Final Output

The consolidated "what to show" folder — pointers to the best representative
artifacts elsewhere in `results/`, for quick access during a demo,
interview, or report submission.

## Key artifacts

| Artifact | Location |
|---|---|
| Motion vs. static waveform/spectrum comparison | `results/Graphs/human_walking_quicklook.png`, `results/Graphs/static_no_motion_quicklook.png` |
| Motion intensity heatmaps | `results/Heatmaps/human_walking_heatmap.png`, `results/Heatmaps/static_no_motion_heatmap.png` |
| Accuracy / performance summary | `results/Performance_Report/Performance_Report.md` |
| Full experiment logs | `experiments/` |
| Tool screenshots | `results/Screenshots/` (add your own captures) |

## Suggested final deliverable bundle

For a placement portfolio or final submission, the minimal set to package
together is:
1. `README.md` (project overview + quick start)
2. `results/Performance_Report/Performance_Report.md`
3. `results/Graphs/` and `results/Heatmaps/` (visual evidence)
4. `presentations/PPT/` deck (built from the outline provided)
5. Link to the GitHub repository itself for full code/reproducibility

Once you've run the system on real hardware, replace the synthetic
example artifacts throughout `datasets/`, `results/`, and
`experiments/Accuracy_Evaluation` with your actual captured data and
re-generate these summary figures using the scripts in
`scripts/Visualization` and `visualization/Heatmaps`.
