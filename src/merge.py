from pathlib import Path
import os
from datetime import datetime, timedelta, timezone

from modules.plotter import *

if __name__ == "__main__":
    JST = timezone(timedelta(hours=+9), "JST")

    # GOOD, タイムゾーンを指定している．早い
    timenow = datetime.now(JST)
    nowstr = timenow.strftime("%Y%m%d_%H_%M_%S")
    p = Path("./results")
    files = list(p.glob("*"))
    file_updates = {file_path: os.stat(file_path).st_mtime for file_path in files}
    path_list = sorted(file_updates, key=file_updates.get)

    with open("./conditions.txt") as f:
        condstr = f.read()

    with open("./tmp.txt") as f:
        rang = f.read()
        print(rang)
        sta, end, ste = map(float, rang.split(","))

    for file_path in path_list[:3]:
        with open(file_path) as f:
            res = f.read()
            xarray = np.arange(sta, end + ste, ste)
            with open("./parsed_results/" + file_path.name, "w+") as f2:
                parsed_data2 = parse_data(res, False)
                f2.write(str(parsed_data2))
                f2.write(str(xarray))
            parsed_data = parse_data(res, True)
            print(rang.split(","))

            plot_data(
                parsed_data=parsed_data,
                xarray=xarray,
                xlabel="Gate Voltage (V)",
                ylabel="Source Current (nA)",
                ylim=[1e-15, 1e-7],
                # TODO: title or legend
                title="Test Nanotransistor",
                # TODO: file name
                out_path="./figures/" + file_path.stem + "mul" + ".png",
            )
