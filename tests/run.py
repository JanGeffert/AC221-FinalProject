# run.py -- runs unit tests

import pandas as pd
import unittest
import os

class Testing(unittest.TestCase):
    def test_csv(self):
        """Check if CSV is valid"""
        df = pd.read_csv("data/data.csv")
        self.assertEqual(df.shape, (30000, 25))

if __name__ == '__main__':
    unittest.main()
