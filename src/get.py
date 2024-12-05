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
    visa_tuple = rm.list_resources()
    print("c")
    # 遅い
    inst = rm.open_resource(visa_tuple[0])
    print("d")
    keithley = Keithley6517B(inst)

    print(keithley.get_idn())

    res = keithley.trace_data()
    print(res)
    # todo: file name
    with open("./conditions.txt") as f:
        condstr = f.read()
        save_data("./results/" + condstr + nowstr + ".txt", res)
