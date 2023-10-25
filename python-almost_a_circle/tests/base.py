#!/usr/bin/python3
"""Unit tests for Base class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_init_id(self):
        """check that the id is assigned"""
        b1 = Base()
        b2 = Base()
        b3 = Base(99)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 99)

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_change_id(self):
        """check if id can change"""
        b1 = Base()
        self.assertAlmostEqual(b1.id, 1)
        b1.id = 50
        self.assertAlmostEqual(b1.id, 50)
        b2 = Base()
        self.assertAlmostEqual(b2.id, 2)

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_nb_objects(self):
        """check if id can change"""
        b1 = Base()
        b2 = Base()
        self.assertAlmostEqual(Base._Base__nb_objects, 2)

    def test_to_json_string(self):
        r1 = Rectangle(1, 1)

    if __name__ == "__main__":
        unittest.main()
