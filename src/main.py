import pyvisa
import time

from keithley_electrometer import *
from plotter import *


if __name__ == "__main__":
    rm = pyvisa.ResourceManager()
    visa_tuple = rm.list_resources()
    inst = rm.open_resource(visa_tuple[0])

    keithley = Keithley6517B(inst)

    print(keithley.get_idn())

    # print(keithley.internal_test())

    keithley.conf_stat_model()

    print(keithley.close_channel(5))

    keithley.set_func_and_range()
    # minimum step size is 5 mV
    keithley.conf_staircase_sweep(0, -1.0, -0.05, 1)

    keithley.run_staircase_sweep()

    # keithley.wait_for_srq()
    # TODO: SRQ
    time.sleep(30)

    res = keithley.trace_data()
    print(res)
    save_data(".res.txt", res)
    parsed_data = parse_data(res)
    xarray = np.arrange(0, -1.05, -0.05)
    plot_data(
        parsed_data=parsed_data,
        xarray=xarray,
        xlabel="Gate Voltage (V)",
        ylabel="Source Current (mA)",
        title="Test Nanotransistor",
        out_path=".test_out.png",
    )
