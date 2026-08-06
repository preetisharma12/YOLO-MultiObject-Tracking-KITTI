from pathlib import Path

summary = Path("/data/pool/bhe-mk3/TrackEval/data/trackers/mot_challenge/KITTI-test/bytetrack_yolov10x/pedestrian_summary.txt")

with open(summary, "r") as f:
    lines = [l.strip().split() for l in f if l.strip()]

headers = lines[0]
combined = lines[-1]

data = dict(zip(headers, combined))

tracker = "ByteTrack YOLOv10x"

# FPS from YOLO tracking speed: about 13.4 ms/frame => 1000 / 13.4
fps = 74.6

print()
print("Higher is better")
print("-" * 70)
print(f"{'Tracker':<22} {'MOTA':>8} {'IDF1':>8} {'HOTA':>8} {'MT':>10} {'Hz/FPS':>10}")
print("-" * 70)
print(
    f"{tracker:<22} "
    f"{float(data['MOTA']):>8.3f} "
    f"{float(data['IDF1']):>8.3f} "
    f"{float(data['HOTA']):>8.3f} "
    f"{float(data['MTR']):>9.3f}% "
    f"{fps:>10.1f}"
)
print()
