import matplotlib.pyplot as plt
import numpy as np


def save_data(data_path: str, data: str):
    with open(data_path, mode="w") as f:
        f.write(data)
    return


def parse_data(data: str, is_abs: bool):
    l = list(data.split(","))
    f = [float(x[:-4]) for x in l[::3]]
    fnp = np.array(f)
    print("raw")
    for x in fnp:
        print(x)
    print()
    if is_abs:
        fnp = np.abs(fnp)
        print("abs")
        for x in fnp:
            print(x)

    return fnp


def plot_data(
    parsed_data: list,
    xarray: list,
    xlabel: str,
    ylabel: str,
    ylim: list,
    title: str,
):
    plt.plot(xarray, parsed_data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylim(ylim)
    plt.yscale("log")
    plt.ylabel(ylabel)
    # plt.show()
    
    return

def save_fig(out_path: str):
    plt.savefig(out_path)