# Paper Draft

Structure for a short conference/workshop-style paper (IEEE two-column
format is common for embedded-systems/radar-sensing work):

## Suggested outline

1. **Abstract** — 150-250 words summarizing motivation, method, and key
   result (e.g. detection accuracy at a given range/material)
2. **Introduction** — motivation (from `docs/Project_Overview.md`), related
   work (from `docs/Literature_Review/README.md`)
3. **System Design**
   - Hardware (radar module, ESP32) — `hardware/`
   - Firmware — `firmware/`
   - Signal processing pipeline — `signal_processing/`
4. **Methodology** — sampling rate, filtering approach, FFT windowing,
   threshold-based detection — pull directly from the relevant subfolder
   READMEs, which already document the rationale for each choice
5. **Experimental Results**
   - Accuracy / precision-recall — `experiments/Accuracy_Evaluation`
   - Range test — `experiments/Distance_Test`
   - Wall-material attenuation — `experiments/Different_Walls`
   - Multi-target limitation — `experiments/Multi_Target`
6. **Discussion** — limitations (single-channel, no range, no direction —
   see `signal_processing/Doppler_Analysis/README.md`)
7. **Conclusion & Future Work** — from the top-level README's Future
   Improvements section
8. **References** — populate from `docs/Literature_Review/README.md`

## Files to add
- [ ] `paper_draft.docx` or `.tex` source
- [ ] Figures exported from `results/Graphs` and `results/Heatmaps`
- [ ] Bibliography (`.bib`) matching `docs/Literature_Review`
