import matplotlib.pyplot as plt
import numpy as np


def save_data(data_path: str, data: str):
    with open(data_path, mode="w") as f:
        f.write(data)
    return


# TODO: 単位を引数で指定
def parse_data(data: str) -> list:
    l = list(data.split(","))
    f = [float(x[:-4]) * 1000 for x in l[::3]]
    return f


def plot_data(
    parsed_data: list, xarray: list, xlabel: str, ylabel: str, title: str, out_path: str
):
    plt.scatter(xarray, parsed_data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylim([0, 2.5])
    plt.ylabel(ylabel)
    # plt.show()
    plt.savefig(out_path)
    return
