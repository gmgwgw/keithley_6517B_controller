import pyvisa
from datetime import datetime, timedelta, timezone

from modules.keithley_electrometer import *
from modules.plotter import *


if __name__ == "__main__":
    JST = timezone(timedelta(hours=+9), "JST")
    timenow = datetime.now(JST)
    nowstr = timenow.strftime("%Y%m%d_%H_%M_%S")

    print("a")
    rm = pyvisa.ResourceManager()
    print("b")
    # 遅い
    inst = rm.open_resource("GPIB0::27::INSTR")
    print("d")
    keithley = Keithley6517B(inst)

    print(keithley.get_idn())

    res = keithley.trace_data()
    print(res)
    # todo: file name
    with open("./conditions.txt") as f:
        condstr = f.read()
        save_data("./results/" + condstr + nowstr + ".txt", res)
