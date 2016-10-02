import pandas as pd
import unittest
from main import main


class TestMain(unittest.TestCase):
    def test_main(self):
        got = main('crimes_small.csv')
        expected_as_dict = {
            'index': [0, 1, 2, 3, 4, 5, 6, 7],
            'data': [
                ['Jan', 'A', 0.14285714285714285],
                ['Jan', 'D', 0.14285714285714285],
                ['Jan', 'E', 0.14285714285714285],
                ['Jan', 'F', 0.14285714285714285],
                ['Jan', 'H', 0.14285714285714285],
                ['Jan', 'I', 0.2857142857142857],
                ['Feb', 'B', 1.0],
                ['Nov', 'A', 1.0],
            ],
            'columns': ['month', 'district', 'demand_index']
        }
        expected = pd.DataFrame(**expected_as_dict)
        pd.util.testing.assert_frame_equal(got, expected)
