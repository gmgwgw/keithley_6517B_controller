import numpy as np

from modules.datamodel import TransistorData


def calc_threshold_voltage(data: TransistorData) -> float:
    return


def calc_sensitivity(data: TransistorData, vrange: list) -> float:
    return


def calc_standard_deviation(data_list: list[TransistorData], volatge: float) -> float:
    curr_at_list = []
    for data in data_list:
        curr_at_list.append(data.curr_at(volatge, 5))
    std = np.std(np.array(curr_at_list))
    return std


def calc_lod(sensitivity: float, blank_sd: float) -> float:
    lod = 3 * blank_sd / sensitivity
    return lod
