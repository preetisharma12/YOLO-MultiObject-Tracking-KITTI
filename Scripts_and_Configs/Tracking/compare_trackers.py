import os

files = {
    "ByteTrack": "/data/pool/bhe-mk3/TrackEval/data/trackers/mot_challenge/KITTI-test/bytetrack_yolov10x/pedestrian_summary.txt",
    "ByteTrack Tuned": "/data/pool/bhe-mk3/TrackEval/data/trackers/mot_challenge/KITTI-test/bytetrack_tuned_yolov10x/pedestrian_summary.txt",
    "BoTSORT": "/data/pool/bhe-mk3/TrackEval/data/trackers/mot_challenge/KITTI-test/botsort_yolov10x/pedestrian_summary.txt",
    "BoTSORT-ReID": "/data/pool/bhe-mk3/TrackEval/data/trackers/mot_challenge/KITTI-test/botsort_reid_yolov10x/pedestrian_summary.txt",
    "OC-SORT": "/data/pool/bhe-mk3/TrackEval/data/trackers/mot_challenge/KITTI-test/ocsort_yolov10x/pedestrian_summary.txt",
    "DeepOCSORT-ReID": "/data/pool/bhe-mk3/TrackEval/data/trackers/mot_challenge/KITTI-test/deepocsort_reid_yolov10x/pedestrian_summary.txt",
    "StrongSORT-ReID": "/data/pool/bhe-mk3/TrackEval/data/trackers/mot_challenge/strongsort_yolov10x/pedestrian_summary.txt",
}

print(f"{'Tracker':18} {'MOTA':>8} {'IDF1':>8} {'HOTA':>8} {'IDSW':>8} {'MT':>8}")
print("-"*75)

for name, path in files.items():

    if not os.path.exists(path):
        print(f"{name:18} MISSING")
        continue

    with open(path) as f:
        header = f.readline().split()
        values = f.readline().split()

    data = dict(zip(header, values))

    print(
        f"{name:18}"
        f"{float(data['MOTA']):8.3f}"
        f"{float(data['IDF1']):8.3f}"
        f"{float(data['HOTA']):8.3f}"
        f"{int(float(data['IDSW'])):8d}"
        f"{int(float(data['MT'])):8d}"
    )
