import json

import pandas as pd
import os
from rectis.geometry.rectangle import Rectangle
from pathlib import Path

def read_instance(file_path):

    if isinstance(file_path, str):
        file_path = Path(file_path)

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File {file_path} not found")

    rectangles = list()

    if file_path.suffix == ".csv":
        instance = pd.read_csv(file_path, header=None, usecols=[2, 3, 4, 5], names=["x1", "y1", "x2", "y2"])
        for _, row in instance.iterrows():
            rectangles.append(Rectangle(x=float(min(row["x1"], row["x2"])),
                                        y=float(min(row["y1"], row["y2"])),
                                        w=float(abs(row["x2"] - row["x1"])),
                                        h=float(abs(row["y2"] - row["y1"]))))
    elif file_path.suffix == ".json":
        with open(file_path, "r") as f:
            data = json.load(f)
            for rect in data["rectangles"]:
                rectangles.append(Rectangle(rect["x"], rect["y"], rect["w"], rect["h"]))
    else:
        raise ValueError("File format not supported")

    return rectangles
