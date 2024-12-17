from pathlib import Path
import numpy as np

from modules.datamodel import *
from modules.analyze import *

def save_data(data_txt_path: Path, raw_data: str):
    """save raw data to txt file

    Args:
        data_txt_path (Path): path to txt file
        raw_data (str): str of the data sent from the instrument
    """
    with open(data_path, mode="w") as f:
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

def calc_mean(data_list: list[TransistorData], meas_label: str = "") -> TransistorData:
    chip_name = data_list[0].chip_name
    transistor_name = data_list[0].transistor_name
    v_start = data_list[0].v_start
    v_end = data_list[0].v_end
    v_step = data_list[0].v_step

    c_data_sum = 0
    for d in data_list:
        c_data_sum += d.c_data

    c_data_average = c_data_sum / len(data_list)
    res = TransistorData(
        chip_name, transistor_name, meas_label, v_start, v_end, v_step, c_data_average
    )
    return res


def calc_log_mean(
    data_list: list[TransistorData], meas_label: str = ""
) -> TransistorData:
    chip_name = data_list[0].chip_name
    transistor_name = data_list[0].transistor_name
    v_start = data_list[0].v_start
    v_end = data_list[0].v_end
    v_step = data_list[0].v_step
    c_data_log_sum = 0

    for d in data_list:
        c_data_log_sum += np.log10(abs(d.c_data))

    c_data_log_average = c_data_log_sum / len(data_list)
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

def read_txt_from_folder(dir_path: Path, meas_label: str="") -> list[TransistorData]:
    file_path_list = list(dir_path.glob("*"))
    data_list = []
    for file_path in file_path_list:
        with open(file_path, "r") as f:
            raw_data = f.read()
        c_data = extract_curr_list(raw_data)
        # TODO: chip name
        data = TransistorData(
            ChipName.SQUARE, "A13", meas_label, 0.2, -1.0, -0.005, c_data
        )
        data_list.append(data)
    return data_list

def calc_mean_in_folder(dir_path: Path, meas_label: str, log: bool=False) -> TransistorData:
    data_list = read_txt_from_folder(dir_path, meas_label)
    if log:
        data_average = calc_log_mean(data_list, meas_label)
    else:
        data_average = calc_mean(data_list, meas_label)
    return data_average

def calc_sd_in_folder(dir_path: Path, voltage: float):
    data_list = read_txt_from_folder(dir_path)
    res = calc_standard_deviation(data_list, voltage)
    return res