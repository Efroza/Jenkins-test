# test_data_operations.py
import unittest
from data_operations import (
    sum_numbers,
    find_average,
    filter_positive_numbers,
    count_occurrences,
    sort_numbers,
    find_maximum,
    find_minimum,
)

class TestDataOperations(unittest.TestCase):

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_numbers([-1, -2, 3, 4, -5]), -1)

    def test_find_average(self):
        self.assertAlmostEqual(find_average([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(find_average([10, 20, 30, 40, 50]), 30.0)
        self.assertIsNone(find_average([]))

    def test_filter_positive_numbers(self):
        self.assertEqual(filter_positive_numbers([1, -2, 3, -4, 5]), [1, 3, 5])
        self.assertEqual(filter_positive_numbers([-1, -2, -3, -4, -5]), [])

    def test_count_occurrences(self):
        data_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        self.assertEqual(count_occurrences(data_list, 2), 2)
        self.assertEqual(count_occurrences(data_list, 3), 3)
        self.assertEqual(count_occurrences(data_list, 5), 0)

    def test_sort_numbers(self):
        self.assertEqual(sort_numbers([5, 2, 4, 1, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(sort_numbers([10, -5, 0, 20]), [-5, 0, 10, 20])

    def test_find_maximum(self):
        self.assertEqual(find_maximum([1, 2, 3, 4, 5]), 5)
        self.assertEqual(find_maximum([-1, -2, -3, -4, -5]), -1)

    def test_find_minimum(self):
        self.assertEqual(find_minimum([1, 2, 3, 4, 5]), 1)
        self.assertEqual(find_minimum([-1, -2, -3, -4, -5]), -5)

if __name__ == "__main__":
    unittest.main()
