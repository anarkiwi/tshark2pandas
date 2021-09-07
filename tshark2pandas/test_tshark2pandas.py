#!/usr/bin/python3

import os
import unittest
import tempfile
import pandas as pd
from tshark2pandas import tshark2pandas


class Tshark2PandasTestCase(unittest.TestCase):

    def test_tshark2pandas(self):
        df = tshark2pandas(os.path.join(os.path.dirname(__file__), 'test.cap'))
        self.assertEqual(10, len(df))
        self.assertEqual(10 * 98, df['frame.cap_len'].sum(), list(df.columns))
    

if __name__ == '__main__':
    unittest.main()
