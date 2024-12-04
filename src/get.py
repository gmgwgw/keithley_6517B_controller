import pyvisa
from datetime import datetime, timedelta, timezone

from keithley_electrometer import *
from plotter import *


if __name__ == "__main__":
    JST = timezone(timedelta(hours=+9), 'JST')

    # GOOD, タイムゾーンを指定している．早い
    timenow = str(datetime.now(JST))
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
    save_data(".res.txt", res)
