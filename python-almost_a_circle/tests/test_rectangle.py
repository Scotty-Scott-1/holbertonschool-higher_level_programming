#!/usr/bin/python3
"""unit test for rectangle"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        """test id"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_invalid_width(self):
        """test invalid width"""
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 5)

    def test_negative_width(self):
        """negative width"""
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 5)

    def test_zero_value_width(self):
        """width 0"""
        with self.assertRaises(ValueError):
            r = Rectangle(0, 6)

    def test_invalid_height(self):
        """invalid height"""
        with self.assertRaises(TypeError):
            r = Rectangle(5, "invalid")

    def test_negative_height(self):
        """negatice height"""
        with self.assertRaises(ValueError):
            r = Rectangle(5, -5)

    def test_zero_value_width(self):
        """0 width"""
        with self.assertRaises(ValueError):
            r = Rectangle(4, 0)

    def test_invalid_x(self):
        """invalid x"""
        with self.assertRaises(TypeError):
            r = Rectangle(5, 5, "invalid", 0)

    def test_negative_x(self):
        """negative x"""
        with self.assertRaises(ValueError):
            r = Rectangle(5, 5, -5, 0)

    def test_invalid_y(self):
        """invalid y"""
        with self.assertRaises(TypeError):
            r = Rectangle(5, 5, 0, "invalid")

    def test_negative_y(self):
        """negative y"""
        with self.assertRaises(ValueError):
            r = Rectangle(5, 5, 0, -5)

    def test_area_evaluation(self):
        """area"""
        r4 = Rectangle(3, 2)
        r5 = Rectangle(2, 10)
        r6 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r4.area(), 6)
        self.assertEqual(r5.area(), 20)
        self.assertEqual(r6.area(), 56)

    def test_str_method(self):
        # [Rectangle] (<id>) <x>/<y> - <width>/<height>
        Base._Base__nb_objects = 0
        r9 = Rectangle(4, 6, 2, 1, 12)
        r10 = Rectangle(5, 5, 1)
        self.assertEqual(r9.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(r10.__str__(), "[Rectangle] (1) 1/0 - 5/5")

    def test_update(self):
        """test update"""
        r13 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r13.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r13.update(89)
        self.assertEqual(r13.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r13.update(89, 2)
        self.assertEqual(r13.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r13.update(89, 2, 3)
        self.assertEqual(r13.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r13.update(89, 2, 3, 4)
        self.assertEqual(r13.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r13.update(89, 2, 3, 4, 5)
        self.assertEqual(r13.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """test update kwargs"""
        r14 = Rectangle(10, 10, 10, 10)
        r14.update(height=1)
        self.assertEqual(r14.__str__(), "[Rectangle] (1) 10/10 - 10/1")
        r14.update(width=1, x=2)
        self.assertEqual(r14.__str__(), "[Rectangle] (1) 2/10 - 1/1")
        r14.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r14.__str__(), "[Rectangle] (89) 3/1 - 2/1")
        r14.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r14.__str__(), "[Rectangle] (89) 1/3 - 4/2")


class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        """id"""
        instance1 = Square(5)
        instance2 = Square(5, 0, 0, 9)
        instance3 = Square(7, 5, 3)
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 9)
        self.assertEqual(instance3.id, 2)

    def test_str_method3(self):
        """str"""
        Base._Base__nb_objects = 0
        s3 = Square(5)
        s4 = Square(2, 2)
        s5 = Square(3, 1, 3)
        self.assertEqual(s3.__str__(), "[Square] (1) 0/0 - 5")
        self.assertEqual(s4.__str__(), "[Square] (2) 2/0 - 2")
        self.assertEqual(s5.__str__(), "[Square] (3) 1/3 - 3")

    def test_invalid_size(self):
        """invalid size"""
        with self.assertRaises(TypeError):
            s = Square("invalid")

    def test_zero_value_size(self):
        """0 width"""
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_update_kwargs2(self):
        """kwargs"""
        s1 = Square(5)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 12/1 - 7")


if __name__ == '__main__':
    unittest.main()
