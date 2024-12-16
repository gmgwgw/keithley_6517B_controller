from enum import Enum
from pathlib import Path
import numpy as np

from modules.datamodel import *

c_data = np.ones(10)
transistordata_test = TransistorData(ChipName.SQUARE, "Z99", 1, 0.0, -1.0, -0.1, c_data)
