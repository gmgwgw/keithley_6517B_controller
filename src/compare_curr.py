from pathlib import Path

from modules.process import *
from modules.datamodel import *
from modules.analyze import *
from modules.plot import *

# transistor only
dir_path_bare = Path("./20241227/bare/")
data_average_f = calc_mean_in_folder(dir_path_bare, "bare")
sd_f = calc_sd_in_folder(dir_path_bare, -0.5)

# bare Au
dir_path_before = Path("./20241227/before")
data_average_b = calc_mean_in_folder(dir_path_before, "before")
sd_b = calc_sd_in_folder(dir_path_before, -0.5)

# ninta0ug
dir_path_after = Path("./20241227/after")
data_average_0 = calc_mean_in_folder(dir_path_after, "after")
sd_0 = calc_sd_in_folder(dir_path_after, -0.5)

# # ninta10ug
# dir_path_10 = Path("./data/to_be_analyzed/ninta10ug")
# data_average_10 = calc_mean_in_folder(dir_path_10, "Ni(Ⅱ)-NTA with BSA (10μg/mL)")
# sd_10 = calc_sd_in_folder(dir_path_10, -0.5)


data_list_for_comparison = [
    data_average_f,
    data_average_b,
    data_average_0,
    # data_average_10,
]

sds = [sd_f, sd_b, sd_0]
print(data_list_for_comparison)
for i in range(3):
    print("SD ", data_list_for_comparison[i].meas_label, sds[i])

for x in data_list_for_comparison:
    print(x.meas_label, "   ", x.curr_at(-0.5, 5), "A")
