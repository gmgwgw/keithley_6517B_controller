import pyvisa
import sys

from modules.keithley_electrometer import *
from modules.plotter import *


if __name__ == "__main__":
    # TODO: 動作確認
    args = sys.argv
    print(args)
    rev = bool(args[1])
    if rev:
        sta = float(args[3])
        end = float(args[2])
        ste = -float(args[4])
    else:
        sta = float(args[2])
        en = float(args[3])
        ste = float(args[4])
    with open("./tmp.txt", 'w') as f:
        f.write("{},{},{}".format(sta, end, ste))

    rm = pyvisa.ResourceManager()
    visa_tuple = rm.list_resources()
    inst = rm.open_resource(visa_tuple[0])

    keithley = Keithley6517B(inst)

    print(keithley.get_idn())

    # print(keithley.internal_test())

    keithley.conf_stat_model()

    print(keithley.close_channel(1))

    keithley.set_func_and_range()
    # minimum step size is 5 mV
    keithley.conf_staircase_sweep(sta, end, ste, 1)

    keithley.run_staircase_sweep()
