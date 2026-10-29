"""Run a pretrained YOLO model on a video and report FPS and detection counts.

Usage:
    python src/detection/baseline_yolo.py --video data/raw/clip1.mp4 --model yolov8n.pt
"""
import argparse
import time
from collections import Counter

import cv2
from ultralytics import YOLO


def run_baseline(video_path: str, model_name: str = "yolov8n.pt", save_path: str = "runs/baseline_out.mp4"):
    model = YOLO(model_name)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise FileNotFoundError(f"Cannot open video: {video_path}")

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    src_fps = cap.get(cv2.CAP_PROP_FPS) or 25

    import os
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*"mp4v"), src_fps, (width, height))

    class_counts = Counter()
    frames = 0
    infer_time = 0.0

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        start = time.perf_counter()
        result = model(frame, verbose=False)[0]
        infer_time += time.perf_counter() - start

        for cls_id in result.boxes.cls.tolist():
            class_counts[result.names[int(cls_id)]] += 1

        writer.write(result.plot())
        frames += 1

    cap.release()
    writer.release()

    fps = frames / infer_time if infer_time > 0 else 0
    print(f"Model: {model_name}")
    print(f"Frames processed: {frames}")
    print(f"Average inference FPS: {fps:.1f}")
    print("Detections by class (top 8):")
    for name, count in class_counts.most_common(8):
        print(f"  {name}: {count}")
    print(f"Annotated video saved to: {save_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", required=True)
    parser.add_argument("--model", default="yolov8n.pt")
    parser.add_argument("--out", default="runs/baseline_out.mp4")
    args = parser.parse_args()
    run_baseline(args.video, args.model, args.out)


if __name__ == "__main__":
    main()