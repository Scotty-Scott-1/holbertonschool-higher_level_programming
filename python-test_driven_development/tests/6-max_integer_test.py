#!/usr/bin/python3
"""Module to find the max integer in a list
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_normal(self):
        max_integer([1, 2, 3, 4])
        result = 4
        self.assertEqual(result, 4)

    def test_normal2(self):
        max_integer([1, 2, 3, 4, 50])
        result = 50
        self.assertEqual(result, 50)

    def test_empty_list(self):
        max_integer([])
        result = None
        self.assertEqual(result, None)

    def test_negative(self):
        max_integer([-1, -2, -3, -4, -50])
        result = -1
        self.assertEqual(result, -1)

    def test_string(self):
        max_integer(["abczde"])
        result = "z"
        self.assertEqual(result, "z")

    def test_char(self):
        max_integer(["e"])
        result = "e"
        self.assertEqual(result, "e")

    def test_float(self):
        max_integer([1.00, 1.01, 1.02, 1.03])
        result = 1.03
        self.assertEqual(result, 1.03)

    if __name__ == "__main__":
        unittest.main()
