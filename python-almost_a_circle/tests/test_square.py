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
        expected = ("__init__() missing 1 required "
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
        expected = ("__init__() takes from 2 to 5 "
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

    def test_update_excess_agrs(self):
        """14 test update"""
        s1 = Square(1, 1, 1, 1)
        s1.update(5, 5, 55, 55, 5, 5, 4, 8)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 55)
        self.assertEqual(s1.y, 55)

    def test_update_4_args(self):
        """15 test update"""
        s1 = Square(1, 1, 1, 1)
        s1.update(5, 5, 55, 55)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 55)
        self.assertEqual(s1.y, 55)

    def test_update_3_args(self):
        """14 test update"""
        s1 = Square(1, 1, 1, 1)
        s1.update(5, 5, 55)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 55)
        self.assertEqual(s1.y, 1)

    def test_update_2_args(self):
        """14 test update"""
        s1 = Square(1, 1, 1, 1)
        s1.update(5, 5)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 1)

    def test_update_1_args(self):
        """14 test update"""
        s1 = Square(1, 1, 1, 1)
        s1.update(5)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 1)

    def test_update_0_args(self):
        """14 test update"""
        s1 = Square(1, 1, 1, 1)
        s1.update()
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 1)

    def test_update_4_kwargs(self):
        """14 test update"""
        s1 = Square(1, 1, 1, 1)
        s1.update(id=5, size=5, y=55, x=5)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 55)

    def test_update_3_kwargs(self):
        """14 test update"""
        s1 = Square(1, 1, 1, 1)
        s1.update(id=5, size=5, y=55)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 55)

    def test_update_2_kwargs(self):
        """14 test update"""
        s1 = Square(1, 1, 1, 1)
        s1.update(id=5, size=5)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 1)

    def test_update_1_kwargs(self):
        """14 test update"""
        s1 = Square(1, 1, 1, 1)
        s1.update(size=5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 1)

    def test_update_args_and_kwargs(self):
        """14 test update"""
        s1 = Square(1, 1, 1, 1)
        s1.update(6, 6, 6, 6, id=5, size=5, y=55, x=5)
        self.assertEqual(s1.id, 6)
        self.assertEqual(s1.width, 6)
        self.assertEqual(s1.height, 6)
        self.assertEqual(s1.x, 6)
        self.assertEqual(s1.y, 6)

    def test_to_dict(self):
        s1 = Square(1, 2, 3, 99)
        expected = {"id": 99, "x": 2, "size": 1, "y": 3}
        self.assertEqual(s1.to_dictionary(), expected)

    if __name__ == "__main__":
        unittest.main()
