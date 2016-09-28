import pandas as pd
import unittest
from main import main


class TestMain(unittest.TestCase):
    def test_main(self):
        raw = {
            'index': [0, 1, 2, 3, 4, 5, 6],
            'data': [
                ['Feb', 'B', 1.0],
                ['Jan', 'A', 0.14285714285714285],
                ['Jan', 'D', 0.14285714285714285],
                ['Jan', 'E', 0.14285714285714285],
                ['Jan', 'F', 0.14285714285714285],
                ['Jan', 'H', 0.14285714285714285],
                ['Jan', 'I', 0.2857142857142857],
            ],
            'columns': ['month', 'district', 'demand_index']
        }
        expected = pd.DataFrame(**raw)
        pd.util.testing.assert_frame_equal(main('crimes_small.csv'), expected)
