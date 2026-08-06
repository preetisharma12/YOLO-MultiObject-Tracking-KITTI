from pathlib import Path

trackers = [
    "strongsort_yolo11x",
    "strongsort_yolov8x",
    "strongsort_yolo26s",
    "strongsort_yolo12s",
    "strongsort_yolo11s",
    "strongsort_yolov10s",
    "strongsort_yolov10x",
    "strongsort_yolo26l",
    "strongsort_yolo12x",
    "strongsort_yolo26x",
]

base = Path(
    "/data/pool/bhe-mk3/TrackEval/data/trackers/mot_challenge/KITTI-test"
)

print(
    f"{'Tracker':30s} "
    f"{'MOTA':>8s} "
    f"{'IDF1':>8s} "
    f"{'HOTA':>8s} "
    f"{'IDSW':>8s} "
    f"{'MT':>8s}"
)

print("-" * 80)

for tracker in trackers:

    fpath = base / tracker / "pedestrian_summary.txt"

    if not fpath.exists():
        print(f"{tracker:30s} MISSING")
        continue

    with open(fpath) as f:
        lines = f.readlines()

    header = lines[0].split()
    values = lines[1].split()

    cols = {k: i for i, k in enumerate(header)}

    mota = values[cols["MOTA"]]
    idf1 = values[cols["IDF1"]]
    hota = values[cols["HOTA"]]
    idsw = values[cols["IDSW"]]
    mt = values[cols["MT"]]

    print(
        f"{tracker:30s} "
        f"{mota:>8s} "
        f"{idf1:>8s} "
        f"{hota:>8s} "
        f"{idsw:>8s} "
        f"{mt:>8s}"
    )
