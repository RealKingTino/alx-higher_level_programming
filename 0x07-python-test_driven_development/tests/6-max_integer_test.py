#!/usr/bin/python3
"""Unittest for max_integer(list)
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class to perform unittests for max_integer(list)
    """

    def test_empty_list(self):
        """Test when the list is empty
        """
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test when the list contains a single element
        """
        self.assertEqual(max_integer([4]), 4)

    def test_positive_numbers(self):
        """Test when the list contains positive numbers
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([10, 20, 30, 40]), 40)

    def test_negative_numbers(self):
        """Test when the list contains negative numbers
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -20, -30, -40]), -10)

    def test_mixed_numbers(self):
        """Test when the list contains mixed positive and negative numbers
        """
        self.assertEqual(max_integer([1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([10, -20, 30, -40]), 30)

    def test_duplicate_numbers(self):
        """Test when the list contains duplicate numbers
        """
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([5, 5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([-5, -5, -5, -5]), -5)

if __name__ == '__main__':
    unittest.main()
