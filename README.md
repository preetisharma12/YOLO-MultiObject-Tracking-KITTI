# Detection and Tracking Project

This repository contains all trained models, tracking results, scripts, configurations, and reference links used for the object detection and multi-object tracking experiments on the KITTI dataset.

---

# Project Structure

```
Detection_and_Tracking/
│
├── Detection/
│   ├── YOLO_Detectors.tar.gz
│   └── OSNet_ReID.tar.gz
│
├── Tracking/
│   └── Trackers_Results.tar.gz
│
├── Scripts_and_Configs/
│   ├── Detection/
│   ├── Tracking/
│   └── Requirements.md
│
├── References/
│   ├── YOLO_Model_Links.md
│   └── Tracker_Links.md
│
└── README.md
```

---

# Folder Description

## Detection

Contains all trained YOLO detector models and the KITTI-trained OSNet Re-Identification (ReID) model.

### YOLO_Detectors.tar.gz

Includes the complete training folders for all detector models:

- YOLOv8x
- YOLOv10s
- YOLOv10x
- YOLO11s
- YOLO11x
- YOLO12s
- YOLO12x
- YOLO26s
- YOLO26l
- YOLO26x

Each training folder contains:

- best.pt
- last.pt
- training logs
- results.csv
- results.png
- confusion matrices
- training arguments (args.yaml)

### OSNet_ReID.tar.gz

Contains the KITTI-trained OSNet Re-Identification model, including:

- Trained OSNet model (.pth)
- ONNX model (.onnx)
- Training checkpoints
- ReID project files

---

## Tracking

Contains the tracking results generated using:

- StrongSORT++
- DeepOCSORT-ReID

Each tracker folder contains:

- Tracking output
- TrackEval results
- Summary metrics
- Detailed metrics
- Evaluation plots

---

## Scripts_and_Configs

Contains all scripts and configuration files used during the project.

### Detection

- Training_Command.txt
- YOLO_Training_Args.yaml

### Tracking

Contains the scripts used to:

- Run StrongSORT++
- Run DeepOCSORT-ReID
- Evaluate tracking performance using TrackEval
- Generate comparison tables
- Generate evaluation plots

### Requirements.md

Lists the software and hardware requirements used during the project.

---

## References

Contains external resources used during the project.

### YOLO_Model_Links.md

Download links for all pretrained YOLO models.

### Tracker_Links.md

Repository and paper links for:

- StrongSORT++
- DeepOCSORT

---

# Dataset

Experiments were performed using:

- KITTI Object Detection Dataset
- KITTI Tracking Dataset

---

# Project Pipeline

```
KITTI Dataset
      │
      ▼
YOLO Detector Training
      │
      ▼
OSNet ReID Training
      │
      ▼
StrongSORT++ / DeepOCSORT-ReID
      │
      ▼
Tracking Results
      │
      ▼
TrackEval Evaluation
      │
      ▼
Performance Comparison
```

---

# Outputs

This project contains:

- Trained YOLO detector models
- KITTI-trained OSNet ReID model
- StrongSORT++ tracking results
- DeepOCSORT-ReID tracking results
- TrackEval evaluation reports
- Evaluation plots
- Training configurations
- Tracking scripts
- Reference links

---

# Author

Preeti Sharma

M.Sc. Information Technology

TH OWL, Germany

