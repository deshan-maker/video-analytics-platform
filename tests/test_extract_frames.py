import cv2
import numpy as np
import pytest

from src.data.extract_frames import extract_frames


def make_dummy_video(path, n_frames=30, size=(64, 64)):
    """Create a tiny video with n_frames random frames for testing."""
    writer = cv2.VideoWriter(str(path), cv2.VideoWriter_fourcc(*"mp4v"), 10, size)
    for _ in range(n_frames):
        frame = np.random.randint(0, 255, (size[1], size[0], 3), dtype=np.uint8)
        writer.write(frame)
    writer.release()


def test_saves_every_nth_frame(tmp_path):
    video = tmp_path / "dummy.mp4"
    make_dummy_video(video, n_frames=30)
    out = tmp_path / "frames"

    saved = extract_frames(str(video), str(out), every=10)

    assert saved == 3
    assert len(list(out.glob("*.jpg"))) == 3


def test_missing_video_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        extract_frames(str(tmp_path / "nope.mp4"), str(tmp_path / "out"))


def test_invalid_every_raises(tmp_path):
    with pytest.raises(ValueError):
        extract_frames("any.mp4", str(tmp_path / "out"), every=0)