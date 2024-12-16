from pathlib import Path
import numpy as np


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
