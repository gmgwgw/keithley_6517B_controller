import os
from pathlib import Path

from keithley_6517B_controller.src.modules.process import *
from modules.datamodel import *
from modules.plot import *

dir_path = Path("./data/results")
file_path_list = list(dir_path.glob("*"))

print("Checking ", file_path_list)

file_updates = {file_path: os.stat(file_path).st_mtime for file_path in file_path_list}
file_path = sorted(file_updates, key=file_updates.get)[0]

with open(file_path, "r") as f:
    raw_data = f.read()
c_data = extract_curr_list(raw_data)
data = TransistorData(ChipName.SQUARE, "A13", "for check", -0.2, -1.0, -0.005, c_data)
print(data.info())


plot_data_list(
    [data],
    xlabel="Gate Voltage (V)",
    ylabel="Source Current (A)",
    ylim=[1e-12, 1e-4],
    title="just checking",
)

save_fig("./figures")
