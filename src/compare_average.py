from pathlib import Path

from modules.process import *
from modules.datamodel import *
from modules.analyze import *
from modules.plot import *


# # transistor only
# dir_path_f = Path("./data/fetonly")
# data_average_f = calc_mean_in_folder(dir_path_f, "Transistor only", True)

# bare Au
# dir_path_b = Path("./data/bare")
# data_average_b = calc_mean_in_folder(dir_path_b, "Bare Au", True)

# ninta0ug
dir_path_0 = Path("./data/ninta0ug")
data_average_0 = calc_mean_in_folder(dir_path_0, "Ni(Ⅱ)-NTA")

# ninta10ug
dir_path_10 = Path("./data/ninta10ug")
data_average_10 = calc_mean_in_folder(dir_path_10, "Ni(Ⅱ)-NTA with BSA (10μg/mL)")

# dir_path_ba = Path("./data/bare")
# data_average_ba = calc_mean_in_folder(dir_path_ba, "Au")

# dir_path_be = Path("./data/before")
# data_average_be = calc_mean_in_folder(dir_path_be, "before hybridization")

# dir_path_af = Path("./data/after")
# data_average_af = calc_mean_in_folder(dir_path_af, "after hybridization")

data_list_for_comparison = [
    # data_average_f,
    # data_average_b,
    data_average_0,
    data_average_10,
    # data_average_ba,
    # data_average_be,
    # data_average_af
]

plot_data_list(
    data_list_for_comparison,
    xlabel="Gate Voltage (V)",
    ylabel="Source Current (A)",
    ylim=[1e-10, 1e-6],
    title="I-Vg curve of nanotransistor with extended gate (DNA probe)",
    xline=-0.5,
)

save_fig("./20250120.png")
