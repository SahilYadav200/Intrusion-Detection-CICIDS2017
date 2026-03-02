"""
Basic tests for data preprocessing utilities used in the Intrusion Detection project.
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.preprocessing import (
    remove_duplicates,
    handle_missing_values,
    normalize,
    encode_labels,
)


class TestRemoveDuplicates(unittest.TestCase):
    def test_no_duplicates(self):
        data = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(remove_duplicates(data), data)

    def test_with_duplicates(self):
        data = [[1, 2], [1, 2], [3, 4]]
        self.assertEqual(remove_duplicates(data), [[1, 2], [3, 4]])

    def test_all_duplicates(self):
        data = [[0, 0], [0, 0]]
        self.assertEqual(remove_duplicates(data), [[0, 0]])

    def test_empty(self):
        self.assertEqual(remove_duplicates([]), [])


class TestHandleMissingValues(unittest.TestCase):
    def test_no_missing(self):
        data = [[1, 2], [3, 4]]
        self.assertEqual(handle_missing_values(data), data)

    def test_none_replaced(self):
        data = [[1, None], [None, 4]]
        self.assertEqual(handle_missing_values(data), [[1, 0], [0, 4]])

    def test_nan_replaced(self):
        data = [[float('nan'), 2.0]]
        result = handle_missing_values(data)
        self.assertEqual(result, [[0, 2.0]])

    def test_custom_fill_value(self):
        data = [[None, 1]]
        self.assertEqual(handle_missing_values(data, fill_value=-1), [[-1, 1]])


class TestNormalize(unittest.TestCase):
    def test_basic(self):
        result = normalize([0, 5, 10])
        self.assertAlmostEqual(result[0], 0.0)
        self.assertAlmostEqual(result[1], 0.5)
        self.assertAlmostEqual(result[2], 1.0)

    def test_constant_values(self):
        result = normalize([3, 3, 3])
        self.assertEqual(result, [0.0, 0.0, 0.0])

    def test_single_element(self):
        result = normalize([7])
        self.assertEqual(result, [0.0])


class TestEncodeLabels(unittest.TestCase):
    def test_benign_and_attack(self):
        labels = ['BENIGN', 'DoS', 'BENIGN', 'DoS']
        encoded, mapping = encode_labels(labels)
        self.assertEqual(len(mapping), 2)
        self.assertEqual(encoded[0], encoded[2])
        self.assertEqual(encoded[1], encoded[3])
        self.assertNotEqual(encoded[0], encoded[1])

    def test_single_class(self):
        labels = ['BENIGN', 'BENIGN']
        encoded, mapping = encode_labels(labels)
        self.assertEqual(encoded, [0, 0])
        self.assertEqual(mapping, {'BENIGN': 0})

    def test_ordering(self):
        labels = ['Z', 'A', 'M']
        encoded, mapping = encode_labels(labels)
        self.assertEqual(mapping['A'], 0)
        self.assertEqual(mapping['M'], 1)
        self.assertEqual(mapping['Z'], 2)


if __name__ == '__main__':
    unittest.main()
