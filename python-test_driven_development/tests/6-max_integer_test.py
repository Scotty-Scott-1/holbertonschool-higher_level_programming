#!/usr/bin/python3
"""Module to find the max integer in a list
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_iteger(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4, 50]), 50)
        self.assertEqual(max_integer([100, 2, 3, 4, 50]), 100)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1, -2, -3, -4, -50]), -1)
        self.assertEqual(max_integer("abczde"), "z")
        self.assertEqual(max_integer(["e"]), "e")
        self.assertEqual(max_integer([1.00, 1.01, 1.02, 1.03]), 1.03)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 1]), 1)


    if __name__ == "__main__":
        unittest.main()
