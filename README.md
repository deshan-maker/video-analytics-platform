# Video Analytics Platform

![CI](https://github.com/deshan-maker/video-analytics-platform/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Real-time vehicle detection, tracking, counting and traffic forecasting from video.

![demo](docs/demo.gif)

*Pretrained YOLOv8 baseline on my own phone footage.*

## Status

- [x] **Phase 1:** Data and baseline ([v0.1](https://github.com/deshan-maker/video-analytics-platform/releases))
- [ ] Phase 2: Fine-tuned detection on traffic data
- [ ] Phase 3: Tracking and line-crossing counter
- [ ] Phase 4: Forecasting and anomaly detection
- [ ] Phase 5: API and dashboard
- [ ] Phase 6: Optimization (ONNX) and deployment

## Baseline results

Pretrained YOLOv8 (COCO) on CPU, 726 frames of road traffic recorded on a phone.

| Model | Avg FPS (CPU) | car | truck | bus | person | motorcycle |
|---|---|---|---|---|---|---|
| yolov8n | 7.7 | 2890 | 309 | 233 | 150 | 90 |
| yolov8s | 3.0 | 2859 | 756 | 292 | 195 | 134 |

Key takeaways:

- Both models run far below real-time speed on CPU, which motivates the optimization work in Phase 6.
- Counts are per-frame totals, not unique vehicles. Tracking (Phase 3) is needed for real counts.
- COCO has no tuk-tuk class, so three-wheelers can be mislabeled. Fine-tuning (Phase 2) targets this.
- yolov8s reports many more trucks than yolov8n; without ground-truth labels it is unclear how many are correct.

Full notes are in [docs/experiments.md](docs/experiments.md).

## Project structure

```
src/
  data/          frame extraction
  detection/     YOLO baseline (fine-tuning next)
  tracking/      planned
  forecasting/   planned
  api/           planned
tests/           unit tests
docs/            dataset notes and experiment log
.github/         CI workflow
```

## Setup

```bash
git clone https://github.com/deshan-maker/video-analytics-platform.git
cd video-analytics-platform
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
```

## Usage

Extract frames from a video (every 15th frame):

```bash
python src/data/extract_frames.py --video data/raw/clip_01.mp4 --out data/frames/clip_01 --every 15
```

Run the pretrained YOLO baseline (prints FPS and detection counts, saves an annotated video):

```bash
python src/detection/baseline_yolo.py --video data/raw/clip_01.mp4 --model yolov8n.pt
```

Run the tests:

```bash
pytest
```

## Data

Sources, license and download steps are in [docs/dataset.md](docs/dataset.md).
Datasets, videos and model weights are not stored in this repository.

## Roadmap

Planned work follows the phases in Status above. Progress is tracked with GitHub Issues
and the project board.

## Author

Built by [deshan-maker](https://github.com/deshan-maker) as a portfolio project while
learning deep learning engineering.