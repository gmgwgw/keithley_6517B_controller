import matplotlib.pyplot as plt
import numpy as np

from modules.datamodel import TransistorData


def plot_data_list(
    data_list: list[TransistorData],
    xlabel: str,
    ylabel: str,
    xlim: list,
    ylim: list,
    title: str,
    xline: float,
):
    for transistor_data in data_list:
        v_array = transistor_data.v_array()
        label = transistor_data.meas_label
        plt.plot(v_array, abs(transistor_data.c_data), label=label)
    # plt.yscale("log")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xlim(xlim)
    # plt.ylim(ylim)
    plt.vlines(xline, ylim[0], ylim[1], color="gray", linestyles="dotted")
    plt.legend()
    return


def save_fig(out_path: str):
    plt.savefig(out_path)
