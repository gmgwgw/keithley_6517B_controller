from enum import Enum
from pathlib import Path
import numpy as np


class ChipName(Enum):
    SQUARE = "square chip"
    CIRCLE = "circle chip"


class TransistorData:
    chip_name: ChipName
    transistor_name: str
    meas_label: int
    v_start: float
    v_end: float
    v_step: float
    c_data: np.ndarray

    def __init__(
        self,
        chip_name: ChipName,
        transistor_name: str,
        meas_label: str,
        v_start: float,
        v_end: float,
        v_step: float,
        c_data: np.ndarray,
    ):
        self.chip_name = chip_name
        self.transistor_name = transistor_name
        self.meas_label = meas_label
        self.v_start = v_start
        self.v_end = v_end
        self.v_step = v_step
        self.c_data = c_data

    def info(self) -> str:
        return f"chip_name: {self.chip_name},\ntransistor_name: {self.transistor_name},\nmeas_label: {self.meas_label},\nsource voltage: {self.v_start}V ~ {self.v_end}V, {self.v_step}V/step"

    def load_txt(
        self,
        txt_path: Path,
        chip_name: ChipName,
        transistor_name: str,
        meas_label: int,
        v_start: float,
        v_end: float,
        v_step: float,
    ):
        with open(txt_path) as f:
            f.read()
        return

    def save_csv(self, csv_path: Path):
        with open(file_path, "w") as f:
            # kakikomi
            f.write(self)
            return

    def read_csv(self, csv_path):
        with open(file_path, "r") as f:
            return

    def v_array(self) -> np.ndarray:
        return np.arange(self.v_start, self.v_end, self.v_step)
