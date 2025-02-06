from pathlib import Path
import numpy as np

from modules.datamodel import *
from modules.analyze import *


def save_data(data_txt_path: Path, tmp_str: str, raw_data: str):
    """save raw data to txt file

    Args:
        data_txt_path (Path): path to txt file
        raw_data (str): str of the data sent from the instrument
    """
    data = "{}\n{}".format(tmp_str, raw_data)
    with open(data_txt_path, mode="w") as f:
        f.write(data)
    return


def extract_curr_list(raw_data: str) -> np.ndarray:
    """extract current values from str of raw data

    Args:
        raw_data (str): string of raw data

    Returns:
        np.ndarray: extracted current values
    """
    l = list(raw_data.split(","))
    f = [float(x[:-4]) for x in l[::3]]
    fnp = np.array(f)
    return fnp


def calc_average(
    data_list: list[TransistorData], meas_label: str = ""
) -> TransistorData:
    print(data_list)
    chip_name = ""
    transistor_name = data_list[0].transistor_name
    v_start = data_list[0].v_start
    v_end = data_list[0].v_end
    v_step = data_list[0].v_step
    c_data_average = sum([d.c_data for d in data_list]) / len(data_list)
    res = TransistorData(
        chip_name, transistor_name, meas_label, v_start, v_end, v_step, c_data_average
    )
    return res


def calc_geometric_average(
    data_list: list[TransistorData], meas_label: str = ""
) -> TransistorData:
    chip_name = data_list[0].chip_name
    transistor_name = data_list[0].transistor_name
    v_start = data_list[0].v_start
    v_end = data_list[0].v_end
    v_step = data_list[0].v_step
    c_data_log_average = sum(np.log10(abs([d.c_data for d in data_list]))) / len(
        data_list
    )

    res = TransistorData(
        chip_name,
        transistor_name,
        meas_label,
        v_start,
        v_end,
        v_step,
        10**c_data_log_average,
    )

    return res


def read_txt_from_folder(dir_path: Path, meas_label: str = "") -> list[TransistorData]:
    file_path_list = list(dir_path.glob("*"))
    data_list = []
    for i, file_path in enumerate(file_path_list):
        with open(file_path, "r") as f:
            tmp_data = f.readline()
            raw_data = f.readline()
        v_data = list(map(float, tmp_data.split(",")))
        c_data = extract_curr_list(raw_data)
        # TODO: chip name
        data = TransistorData(ChipName.SQUARE, "A13", str(i + 1), v_data[0], v_data[1], v_data[2], c_data)
        data_list.append(data)
    return data_list

def calc_mean_in_folder(
    dir_path: Path, meas_label: str, log: bool = False
) -> TransistorData:
    data_list = read_txt_from_folder(dir_path, meas_label)
    print(data_list)
    if log:
        data_average = calc_geometric_average(data_list, meas_label)
    else:
        data_average = calc_average(data_list, meas_label)
    return data_average


def calc_sd_in_folder(dir_path: Path, voltage: float):
    data_list = read_txt_from_folder(dir_path)
    res = calc_standard_deviation(data_list, voltage)
    return res
