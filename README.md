# Multi-Object Tracking Benchmark on KITTI: YOLO Detectors x MOT Trackers

Benchmarking 10 YOLO detector variants against multi-object trackers on the KITTI dataset, with a custom-trained Re-ID model, for an intention-aware autonomous navigation use case (MONOCAB project, TH OWL).

---

## Overview

This repository documents object detection and multi-object tracking experiments on the KITTI dataset: detector training, Re-ID model training, tracking, and evaluation with TrackEval.

Headline result: YOLO12x + DeepOCSORT / StrongSORT++ (~88 MOTA, ~80 HOTA) was the best-performing combination found. See Results below.

## Detectors & Trackers

YOLO detector variants (10): YOLOv8x, YOLOv10s, YOLOv10x, YOLO11s, YOLO11x, YOLO12s, YOLO12x, YOLO26s, YOLO26l, YOLO26x.

Trackers: StrongSORT++ and DeepOCSORT-ReID, each paired with a KITTI-trained OSNet Re-ID model (Rank-1 accuracy: 85.8%).

Evaluation: TrackEval (HOTA, MOTA, IDF1, and related metrics).

## Example Outputs

Two visual tracking result videos are included in this repo: [Visual_Tracking_Result_1.mp4](Tracking/Visual_Tracking_Result_1.mp4) and [Visual_Tracking_Result_2.mp4](Tracking/Visual_Tracking_Result_2.mp4).

## Installation

```bash
git clone https://github.com/preetisharma12/YOLO-MultiObject-Tracking-KITTI.git
cd YOLO-MultiObject-Tracking-KITTI
pip install -r requirements.txt
```

TrackEval is not distributed on PyPI - install it separately (see requirements.txt for the command). Full environment details (OS, CUDA, GPU used for this project) are in Scripts_and_Configs/Requirements.md.

Note on trained weights: detector checkpoints, the trained Re-ID model, and raw tracking outputs are not committed to this repository (they don't belong in git history at this size). Use the training command below to reproduce them, or reach out to the author.

## Usage

### 1. Train a detector

Full command and parameter reference: Scripts_and_Configs/Detection/Training_Command.txt (config: YOLO_Training_Args.yaml)

```bash
yolo detect train \
  data=<path-to-kitti-data.yaml> \
  model=<MODEL_PATH> \
  epochs=300 \
  patience=8 \
  batch=8 \
  imgsz=640 \
  augment=True
```

### 2. Run tracking

Tracking scripts live in Scripts_and_Configs/Tracking/. run_kitti.py runs TrackEval against tracker outputs; run_strongsort_10models.py and run_deepocsort_reid_10models.py run each tracker across all 10 detectors.

### 3. Generate comparison tables & plots

extract_strongsort_table.py and extract_deepocsort_table.py extract per-run metrics. make_table.py and show_final_table.py build the comparison table. comparison_plots.py generates evaluation plots.

## Project Structure

This tree reflects what is actually in the repository:

```
YOLO-MultiObject-Tracking-KITTI/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── References/
│   ├── YOLO_Model_Links.md      # download links for pretrained YOLO models
│   └── Tracker_Links.md          # repo/paper links for StrongSORT++, DeepOCSORT
│
├── Scripts_and_Configs/
│   ├── Requirements.md           # full environment spec (OS, GPU, CUDA, libraries)
│   ├── Detection/
│   │   ├── Training_Command.txt  # reproducible YOLO training command + parameter docs
│   │   └── YOLO_Training_Args.yaml
│   └── Tracking/                 # tracking, evaluation, and table/plot generation scripts
│       ├── run_kitti.py
│       ├── run_strongsort_10models.py
│       ├── run_deepocsort_reid_10models.py
│       ├── compare_trackers.py
│       ├── extract_strongsort_table.py
│       ├── extract_deepocsort_table.py
│       ├── make_table.py
│       ├── show_final_table.py
│       └── comparison_plots.py
│
└── Tracking/
    ├── Trackers_Results.tar.gz   # compressed tracking/evaluation outputs
    ├── Visual_Tracking_Result_1.mp4
    └── Visual_Tracking_Result_2.mp4
```

Trained model weights (YOLO detector checkpoints, the OSNet Re-ID model) are intentionally not stored in this repo - see the Installation section above.

## Results

Best combination found: YOLO12x + DeepOCSORT / StrongSORT++, ~88 MOTA, ~80 HOTA.
<img width="1002" height="269" alt="image" src="https://github.com/user-attachments/assets/8a0cdf9d-2e02-4f96-9c92-01c58dbfdae2" />


<img width="692" height="186" alt="image" src="https://github.com/user-attachments/assets/fe17e0b6-6a41-4738-b025-2864cc684f90" />


## Dataset

Experiments were performed on the KITTI Object Detection Dataset and the KITTI Tracking Dataset.

<img width="906" height="382" alt="image" src="https://github.com/user-attachments/assets/0547562f-5ef0-4349-949e-db617b4c8499" />


Dataset access, licensing, and the exact train/val split used are not documented here yet - see References/ for model/tracker links, and add dataset access details if you want this fully reproducible by others.

## Limitations

The benchmark was evaluated on KITTI only, with no cross-dataset validation, so results may not generalize to other driving environments, camera setups, or geographies. This is a benchmark study, not a deployed system — it hasn't been integrated into a live MONOCAB navigation pipeline.

## Future Improvements

extending the tracker/detector grid, or deploying the best combination in a live pipeline.


## License

MIT - see LICENSE.

## Author

Preeti Sharma - M.Sc. Information Technology, TH OWL, Germany
Research conducted as part of the MONOCAB project, supervised by Prof. Dr.-Ing. habil. Ulrich Büker and Omar Gamal.
