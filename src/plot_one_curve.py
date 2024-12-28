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
    data = TransistorData(ChipName.SQUARE, "A13", str(i + 1), -0.5, -1.0, -0.005, c_data)
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

<<<<<<< HEAD
save_fig("./test")
=======
save_fig("./befores_sample3")
>>>>>>> 9588386a120883203589a486d5623cef269729f6
