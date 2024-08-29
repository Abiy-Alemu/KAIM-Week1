# tests/test_data_processing.py

import unittest
from src.data_processing import load_data, clean_data

class TestDataProcessing(unittest.TestCase):

    def test_load_data(self):
        data = load_data('path/to/file')
        self.assertIsNotNone(data)

    def test_clean_data(self):
        raw_data = 'some raw data'
        cleaned_data = clean_data(raw_data)
        self.assertEqual(cleaned_data, 'expected cleaned data')

if __name__ == '__main__':
    unittest.main()
