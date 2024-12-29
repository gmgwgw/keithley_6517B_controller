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
        tmp_data = f.readline()
        raw_data = f.readline()
    v_data = map(float, tmp_data.split(","))
    c_data = extract_curr_list(raw_data)
    # TODO: chip name
    data = TransistorData(ChipName.SQUARE, "A13", str(i + 1), v_data[0], v_data[1], v_data[2], c_data)
    data_list.append(data)
    print(data.info())


plot_data_list(
    data_list,
    xlabel="Gate Voltage (V)",
    ylabel="Source Current (A)",
    ylim=[1e-10, 1e-6],
    title="transfer curve of DNA probe after hybridization",
    xline=-0.5
)

save_fig("./test")
