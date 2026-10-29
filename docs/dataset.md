# Dataset notes

## Sources
- Own clips: clip1.mp4 (phone)
- UA-DETRAC (YOLO format mirror)
  - Link: https://huggingface.co/datasets/thundarstrom/traffic-vehicle-detection
  - License: CC-BY-4.0
  - Images: 23,319 (train 18,655 / val 2,332 / test 2,332)
  - Classes: car, bus, truck, van
  - Resolution: 640x640 (normalized, native 960x540)

## How to download
pip install huggingface_hub
python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='thundarstrom/traffic-vehicle-detection', repo_type='dataset', local_dir='data/ua_detrac')"

## Observations
- Class imbalance: car ~82.5%, bus ~1.6% (to handle in Phase 2)