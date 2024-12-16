import math
from modules.plotter import *


def test_save_data():
    test_data_path = "../testfiles.test.txt"
    test_data = "ABCDE"
    save_data(test_data_path, test_data)
    with open(test_data_path) as f:
        saved_data = f.read()
        assert saved_data == test_data


def test_parse_data():
    test_result = "+002.3615E-03NADC,+0000000.000000secs,+00000RDNG#,+002.3061E-03NADC,+0000000.000000secs,+00001RDNG#"
    expected_result = [2.3615, 2.3061]
    parsed_result = parse_data(test_result)
    assert math.isclose(parsed_result[0], expected_result[0])
    assert math.isclose(parsed_result[1], expected_result[1])
