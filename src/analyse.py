def calc_mean():
    return


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
