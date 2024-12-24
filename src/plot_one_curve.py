from pathlib import Path

from modules.process import *
from modules.datamodel import *
from modules.plot import *

dir_path = Path("./data/results")
file_path_list = list(dir_path.glob("*"))

print(file_path_list)
data_list = []
for i, file_path in enumerate(file_path_list):
    with open(file_path, "r") as f:
        raw_data = f.read()
    c_data = extract_curr_list(raw_data)
    # TODO: chip name
    data = TransistorData(ChipName.SQUARE, "A13", str(i + 1), -0.4, -1.5, -0.005, c_data)
    data_list.append(data)
    print(data.info())


plot_data_list(
    data_list,
    xlabel="Gate Voltage (V)",
    ylabel="Source Current (A)",
    ylim=[1e-14, 1e-4],
    title="transfer curve of nanotransistor with BSA probe (10 μg/mL)",
    xline=-0.5
)

save_fig("./ninta10")
