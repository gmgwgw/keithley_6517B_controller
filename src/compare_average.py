from pathlib import Path

from keithley_6517B_controller.src.modules.process import *
from modules.datamodel import *
from modules.analyze import *
from modules.plot import *


# transistor only
dir_path_f = Path("./data/to_be_analyzed/fetonly")
data_average_f = calc_mean_in_folder(dir_path_f, "Transistor only", True)

# bare Au
dir_path_b = Path("./data/to_be_analyzed/bare")
data_average_b = calc_mean_in_folder(dir_path_b, "Bare Au", True)

# ninta0ug
dir_path_0 = Path("./data/to_be_analyzed/ninta0ug")
data_average_0 = calc_mean_in_folder(dir_path_0, "Ni(Ⅱ)-NTA", True)

# ninta10ug
dir_path_10 = Path("./data/to_be_analyzed/ninta10ug")
data_average_10 = calc_mean_in_folder(dir_path_10, "Ni(Ⅱ)-NTA with BSA (10μg/mL)", True)

data_list_for_comparison = [
    data_average_f,
    data_average_b,
    data_average_0,
    data_average_10,
]

plot_data_list(
    data_list_for_comparison,
    xlabel="Gate Voltage (V)",
    ylabel="Source Current (A)",
    ylim=[1e-12, 1e-4],
    title="Extended gate test",
    xline=-0.5,
)

save_fig("./20241215.png")
