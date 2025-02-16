import pyvisa
from datetime import datetime, timedelta, timezone

from modules.keithley import *
from modules.process import *

GPIB_ADDR = "GPIB0::27::INSTR"

if __name__ == "__main__":
    JST = timezone(timedelta(hours=+9), "JST")
    timenow = datetime.now(JST)
    nowstr = timenow.strftime("%Y%m%d_%H_%M_%S")

    rm = pyvisa.ResourceManager()
    inst = rm.open_resource(GPIB_ADDR)
    keithley = Keithley6517B(inst)

    print("IDN: ", keithley.get_idn())

    res = keithley.trace_data()
    print("*** measurement result ***")
    print(res)

    with open("./tmp/tmp.txt") as f:
        tmpstr = f.read()

    with open("./tmp/conditions.txt") as f:
        condstr = f.read()
        save_data("./data/results/" + condstr + nowstr + ".txt", tmpstr, res)
