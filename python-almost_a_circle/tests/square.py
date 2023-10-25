#!/usr/bin/python3
"""Unit tests for Base class"""


import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):

    def setUp(self):
        """reset number of objs"""
        Base._Base__nb_objects = 0

    def test_init_no_args(self):
        """define a Sqaure with no args"""
        with self.assertRaises(TypeError) as e:
            s1 = Square()
        expected = ("Square.__init__() missing 1 required "
                    "positional argument: 'size'")
        self.assertEqual(str(e.exception), expected)

    def test_init_1_arg(self):
        """define a saure with one arg"""
        s1 = Square(5)
        s2 = Square(5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)

    def test_init_2_arg(self):
        """define a saure with one arg"""
        s1 = Square(5, 5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.width, 5)

    def test_init_3_arg(self):
        """define a saure with one arg"""
        s1 = Square(5, 5, 5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.x, 5)

    def test_init_4_arg(self):
        """define a saure with one arg"""
        s1 = Square(5, 5, 5, 5)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 5)

    def test_init_5_arg(self):
        """define a Sqaure with 5 args"""
        with self.assertRaises(TypeError) as e:
            s1 = Square(5, 5, 5, 5, 5)
        expected = ("Square.__init__() takes from 2 to 5 "
                    "positional arguments but 6 were given")
        self.assertEqual(str(e.exception), expected)

    if __name__ == "__main__":
        unittest.main()
