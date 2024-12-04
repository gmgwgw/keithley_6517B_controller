from datetime import datetime, timedelta, timezone
from plotter import *

if __name__ == "__main__":
    JST = timezone(timedelta(hours=+9), 'JST')

    # GOOD, タイムゾーンを指定している．早い
    timenow = str(datetime.now(JST))
    with open(".res.txt") as f:
        res = f.read()
        parsed_data = parse_data(res, 0, True)
        xarray = np.arange(1.5, -1.55, -0.1)
        plot_data(
            parsed_data=parsed_data,
            xarray=xarray[:len(parsed_data)],
            xlabel="Gate Voltage (V)",
            ylabel="Source Current (nA)",
            ylim=10e-8,
            title="Test Nanotransistor",
            # TODO: file name
            out_path="./sikaku_B16_w_Vds-4.png",
        )