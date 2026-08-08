# Presentation Slide Outline

No `.pptx` file has been generated yet — this is the content outline to
build one from (e.g. via `pptx` tooling, PowerPoint, or Google Slides).
Recommended structure for an 8-10 slide project/placement presentation:

1. **Title** — Through-Wall Human Motion Detection using Microwave Doppler
   Radar and ESP32
2. **Motivation** — limitations of cameras/PIR/ultrasonic; why radar
3. **Working Principle** — Doppler effect diagram (see `docs/Flowcharts`)
4. **System Architecture** — block diagram (see `docs/Block_Diagrams`)
5. **Hardware** — ESP32 + radar module photo, BOM summary
6. **Firmware & Signal Processing Pipeline** — sampling → filtering → FFT →
   detection flowchart
7. **Results** — waveform/spectrum/heatmap screenshots (see
   `results/Graphs`, `results/Heatmaps`), accuracy table from
   `experiments/Accuracy_Evaluation`
8. **Demo** — live demo or short video (see `videos/`)
9. **Challenges & Limitations** — noise, single-target, no range
10. **Future Work** — TinyML, FMCW, wireless streaming
11. **Q&A**

Export the final deck here as `Through_Wall_Motion_Detection.pptx`.
