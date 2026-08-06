summary_file = "/data/pool/bhe-mk3/TrackEval/data/trackers/mot_challenge/KITTI-test/my_tracker/pedestrian_summary.txt"

with open(summary_file, "r") as f:
    headers = f.readline().split()
    values = f.readline().split()

data = dict(zip(headers, values))

print("\nFINAL TRACKING RESULTS\n")

print("+------------+--------+--------+--------+--------+--------+--------+")
print("| Tracker    | HOTA   | MOTA   | MOTP   | IDF1   | DetA   | AssA   |")
print("+------------+--------+--------+--------+--------+--------+--------+")

print(
    f"| ByteTrack | "
    f"{float(data['HOTA']):<6.2f} | "
    f"{float(data['MOTA']):<6.2f} | "
    f"{float(data['MOTP']):<6.2f} | "
    f"{float(data['IDF1']):<6.2f} | "
    f"{float(data['DetA']):<6.2f} | "
    f"{float(data['AssA']):<6.2f} |"
)

print("+------------+--------+--------+--------+--------+--------+--------+")

