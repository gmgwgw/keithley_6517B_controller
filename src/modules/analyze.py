from modules.datamodel import TransistorData


def calc_mean(data_list: list[TransistorData]) -> TransistorData:
    chip_name = data_list[0].chip_name
    transistor_name = data_list[0].transistor_name
    v_start = data_list[0].v_start
    v_end = data_list[0].v_end
    v_step = data_list[0].v_step

    c_data_sum = 0
    for d in data_list:
        c_data_sum += d.c_data

    c_data_average = c_data_sum / len(data_list)
    res = TransistorData(
        chip_name, transistor_name, "average", v_start, v_end, v_step, c_data_average
    )
    return res


def calc_log_mean():
    return


def calc_threshold_voltage():
    return


def calc_sensitivity(data: list, vrange: list) -> float:
    return


def calc_sd(data: list, volatge: float) -> float:
    return


def calc_lod(sensitivity: float, blank_sd: float) -> float:
    lod = 3 * blank_sd / sensitivity
    return lod
