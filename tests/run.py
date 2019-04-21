# run.py -- runs unit tests

import pandas as pd
import unittest
import os

class Testing(unittest.TestCase):
    def test_dummy(self):
        """Dummy test"""
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
