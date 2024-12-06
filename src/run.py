import pyvisa
import sys

from modules.keithley_electrometer import *
from modules.plotter import *


if __name__ == "__main__":
    # TODO: 動作確認
    args = sys.argv
    print("Input: ", args)
    rev = bool(int(args[1]))
    if rev:
        sta = float(args[3])
        end = float(args[2])
        ste = -float(args[4])
    else:
        sta = float(args[2])
        end = float(args[3])
        ste = float(args[4])
    nplc = int(args[5])
    with open("./tmp.txt", "w") as f:
        f.write("{},{},{}".format(sta, end, ste))

    rm = pyvisa.ResourceManager()
    inst = rm.open_resource("GPIB0::27::INSTR")

    keithley = Keithley6517B(inst)

    print(keithley.get_idn())

    # print(keithley.internal_test())

    print(keithley.close_channel(5))
    keithley.conf_stat_model()

    print("Set NPLC: {}".format(nplc))
    keithley.set_func_and_range(nplc)

    # minimum step size is 5 mV
    print("Start staircase sweep measurement from {}V to {}V".format(sta, end))
    keithley.conf_staircase_sweep(sta, end, ste, 1)

    keithley.run_staircase_sweep()
