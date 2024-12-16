import matplotlib.pyplot as plt
import numpy as np


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
    return


def save_fig(out_path: str):
    plt.savefig(out_path)
