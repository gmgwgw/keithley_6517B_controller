import pyvisa
import time
from datetime import datetime, timedelta, timezone
import sys

from keithley_electrometer import *
from plotter import *


if __name__ == "__main__":
    args = sys.argv
    rev = bool(args[0])
    if rev:
        sta = float(args[2])
        end = float(args[1])
        ste = - float(args[3])
    else:
        sta = float(args[1])
        en = float(args[2])
        ste = float(args[3])
    JST = timezone(timedelta(hours=+9), 'JST')

    # GOOD, タイムゾーンを指定している．早い
    timenow = str(datetime.now(JST))

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