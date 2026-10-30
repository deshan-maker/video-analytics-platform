# Experiments

## Baseline: pretrained YOLOv8 (COCO), CPU
Clip: clip_01.mp4 (phone, 726 frames)

| Model | Frames | Avg FPS | car | truck | bus | person | motorcycle |
|---|---|---|---|---|---|---|---|
| yolov8n | 726 | 7.7 | 2890 | 309 | 233 | 150 | 90 |
| yolov8s | 726 | 3.0 | 2859 | 756 | 292 | 195 | 134 |

Observations:
- yolov8s is ~2.5x slower than yolov8n on CPU (3.0 vs 7.7 FPS); both are below real-time (25-30 FPS), so optimization is needed (Phase 6).
- Both models detect cars and trucks in the annotated videos (visual check).
- yolov8s reports many more trucks (756 vs 309). Without ground-truth labels I can't confirm how many are correct.
- False positives with yolov8n: potted plant (2), fire hydrant (1).
- Counts are per-frame totals, not unique vehicles (tracking in Phase 3).
- COCO has no tuk-tuk class, so three-wheelers may be mislabeled; to revisit in Phase 2 with fine-tuning.

Next: label own frames and fine-tune (Phase 2).