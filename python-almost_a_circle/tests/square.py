#!/usr/bin/python3
"""Unit tests for Base class"""


import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):

    def setUp(self):
        """reset number of objs"""
        Base._Base__nb_objects = 0

    def test_init_no_args(self):
        """1 define a Sqaure with no args"""
        with self.assertRaises(TypeError) as e:
            s1 = Square()
        expected = ("Square.__init__() missing 1 required "
                    "positional argument: 'size'")
        self.assertEqual(str(e.exception), expected)

    def test_init_1_arg(self):
        """2 define a saure with one arg"""
        s1 = Square(5)
        s2 = Square(5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)

    def test_init_2_arg(self):
        """3 define a saure with 2 args"""
        s1 = Square(5, 5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.width, 5)

    def test_init_3_arg(self):
        """4 define a saure with 3 args"""
        s1 = Square(5, 5, 5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.x, 5)

    def test_init_4_arg(self):
        """5 define a saure with 4 args"""
        s1 = Square(5, 5, 5, 5)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 5)

    def test_init_5_arg(self):
        """6 define a Sqaure with 5 args"""
        with self.assertRaises(TypeError) as e:
            s1 = Square(5, 5, 5, 5, 5)
        expected = ("Square.__init__() takes from 2 to 5 "
                    "positional arguments but 6 were given")
        self.assertEqual(str(e.exception), expected)

    def test_is_base(self):
        """7 check id sqaure is instance of Base"""
        s1 = Square(1)
        self.assertIsInstance(s1, Base)

    def test_is_rectangle(self):
        """8 check id sqaure is instance of Rectangle"""
        s1 = Square(1)
        self.assertIsInstance(s1, Rectangle)

    def test_size_getter(self):
        """9 test getter size"""
        s1 = Square(1, 1, 1, 1)
        self.assertEqual(s1.size, 1)

    def test_size_setter(self):
        """10 test setter size"""
        s1 = Square(1, 1, 1, 1)
        s1.size = 5
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.width, 5)

    def test_size_setter_NaN(self):
        """11 test setter size"""
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, 1, 1, 1)
            s1.size = "f"
        expected = "width must be an integer"
        self.assertEqual(str(e.exception), expected)

    def test_size_setter_negative(self):
        """12 test setter size"""
        with self.assertRaises(ValueError) as e:
            s1 = Square(1, 1, 1, 1)
            s1.size = -5
        expected = "width must be > 0"
        self.assertEqual(str(e.exception), expected)

    def test_square__str__(self):
        """13 test __str__"""
        s1 = Square(1, 1, 1, 1)
        self.assertEqual(str(s1), "[Square] (1) 1/1 - 1")

    if __name__ == "__main__":
        unittest.main()
