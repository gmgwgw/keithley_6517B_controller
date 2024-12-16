import os
import numpy as np
from pathlib import Path

from modules.preprocess import *
from modules.datamodel import *
from modules.analyze import *

dir_path = Path("./data/to_be_analyzed")
file_path_list = list(dir_path.glob("*"))
print(file_path_list)

data_list = []

for i, file_path in enumerate(file_path_list):
    with open(file_path, "r") as f:
        raw_data = f.read()
    c_data = extract_curr_list(raw_data)
    # TODO: meas_label
    data = TransistorData(ChipName.SQUARE, "A13", str(i + 1), 0.2, -0.1, -0.05, c_data)
    data_list.append(data)
    print(data.info())

data_average = calc_mean(data_list)
print(data_average.info())

