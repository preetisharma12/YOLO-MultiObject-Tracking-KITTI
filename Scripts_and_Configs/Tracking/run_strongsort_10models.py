import cv2
import numpy as np
from pathlib import Path
from ultralytics import YOLO

from boxmot.trackers.bbox.strongsort.strongsort import StrongSort
from boxmot.reid.core.reid import ReID

models = {
    "yolo11x": "/data/pool/bhe-mk3/preeti_yolo/my_runs/yolo11x_kitti-2/weights/best.pt",
    "yolov8x": "/data/pool/bhe-mk3/preeti_yolo/my_runs/yolov8x_kitti/weights/best.pt",
    "yolo26s": "/data/pool/bhe-mk3/runs/yolo26s_kitti/weights/best.pt",
    "yolo12s": "/data/pool/bhe-mk3/runs/yolo12s_kitti/weights/best.pt",
    "yolo11s": "/data/pool/bhe-mk3/runs/yolo11s_kitti/weights/best.pt",
    "yolov10s": "/data/pool/bhe-mk3/runs/yolov10s_kitti/weights/best.pt",
    "yolov10x": "/data/pool/bhe-mk3/preeti_yolo/yolov10/runs/detect/yolov10x_kitti/weights/best.pt",
    "yolo26l": "/data/pool/bhe-mk3/runs/detect/kitti_clean_yolo26l/weights/best.pt",
    "yolo12x": "/data/pool/bhe-mk3/runs/yolo12x_kitti_clean/weights/best.pt",
    "yolo26x": "/data/pool/bhe-mk3/kitti_combined/runs/detect/kitti_combined_yolo26x_v2/weights/best.pt",
}

seq_root = Path("/data/pool/bhe-mk3/kitti_tracking/training/image_02")

for model_name, model_path in models.items():

    print("\n" + "=" * 80)
    print(f"RUNNING STRONGSORT : {model_name}")
    print("=" * 80)

    out_root = Path(
        f"/data/pool/bhe-mk3/kitti_tracking/strongsort_{model_name}"
    )
    out_root.mkdir(parents=True, exist_ok=True)

    model = YOLO(model_path)

    for seq in sorted(
        [p for p in seq_root.iterdir() if p.is_dir() and p.name.isdigit()]
    ):

        print(f"[{model_name}] Sequence {seq.name}")

        labels_dir = out_root / f"seq_{seq.name}" / "labels"
        labels_dir.mkdir(parents=True, exist_ok=True)

        reid = ReID(
            path="/data/pool/bhe-mk3/kitti_mot_project/reid/checkpoints/kitti_osnet_x0_25.pth",
            device="cuda:0"
        )

        tracker = StrongSort(
            reid_model=reid.model
        )

        for img_path in sorted(seq.glob("*.png")):

            frame_id = img_path.stem

            img = cv2.imread(str(img_path))

            if img is None:
                continue

            h, w = img.shape[:2]

            results = model.predict(
                img,
                conf=0.25,
                imgsz=1280,
                verbose=False
            )[0]

            dets = []

            for box in results.boxes:

                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                conf = float(box.conf[0])
                cls = int(box.cls[0])

                dets.append([
                    x1, y1, x2, y2,
                    conf, cls
                ])

            dets = np.array(dets, dtype=float) if dets else np.empty((0, 6), dtype=float)

            tracks = tracker.update(dets, img)

            with open(labels_dir / f"{frame_id}.txt", "w") as f:

                for t in tracks:

                    x1, y1, x2, y2, track_id, conf, cls, _ = t[:8]

                    xc = ((x1 + x2) / 2) / w
                    yc = ((y1 + y2) / 2) / h
                    bw = (x2 - x1) / w
                    bh = (y2 - y1) / h

                    f.write(
                        f"{int(cls)} "
                        f"{xc:.6f} "
                        f"{yc:.6f} "
                        f"{bw:.6f} "
                        f"{bh:.6f} "
                        f"{int(track_id)}\n"
                    )

    print(f"DONE: {model_name}")

print("ALL MODELS FINISHED")
