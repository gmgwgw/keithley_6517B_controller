import pyvisa
import sys

from modules.keithley_electrometer import *
from modules.plotter import *

# number of power line cycles
# If you want to measure current more slowly, please change the value to 10.
NPLC = 1

if __name__ == "__main__":
    args = sys.argv
    print("Command Line Argments: ", args)
    v_start = float(args[1])
    v_end = float(args[2])
    # Step size must be negative if (start) > (end).
    if v_start > v_end:
        v_step = -float(args[3])
    else:
        v_step = float(args[3])

    # save stsw settings to tmp.txt
    with open("./tmp/tmp.txt", "w") as f:
        f.write("{},{},{}".format(v_start, v_end, v_step))

    # start communicating with the instrument
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource("GPIB0::27::INSTR")

    keithley = Keithley6517B(inst)
    print("IDN: ", keithley.get_idn())
    print("Channel closed: ", keithley.close_channel(5))
    keithley.conf_stat_model()
    print("Set NPLC: {}".format(NPLC))
    keithley.set_func_and_range(NPLC)

    # NOTE: Minimum step size is 5 mV.
    print("Start staircase sweep measurement from {}V to {}V.".format(v_start, v_end))
    print("Step size is set to be {}V.".format(stv_stepe))
    keithley.conf_staircase_sweep(v_start, v_end, v_step)
    keithley.run_staircase_sweep()
