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

    newest_file_path = max(file_updates, key=file_updates.get)
    print(newest_file_path)

    with open("./conditions.txt") as f:
        condstr = f.read()

    with open("./tmp.txt") as f:
        rang = f.read()
        print(rang)
        sta, end, ste = map(float, rang.split(","))

    with open(newest_file_path) as f:
        res = f.read()
        parsed_data = parse_data(res, True)
        print(rang.split(","))
        xarray = np.arange(sta, end + ste, ste)

        plot_data(
            parsed_data=parsed_data,
            xarray=xarray[: len(parsed_data)],
            xlabel="Gate Voltage (V)",
            ylabel="Source Current (nA)",
            ylim=10e-8,
            title="Test Nanotransistor",
            # TODO: file name
            out_path="./figures/" + condstr + nowstr + ".png",
        )
