#!/usr/bin/python3
"""Module to test Base methods and attrs"""
import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    """Test base class"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_init(self):
        """initialisation
        (no args)
        """
        b = Base()
        self.assertEqual(b.id, 1)

    def test_init_with_custom_id(self):
        """initialisation with one arg
        (postive number)    
        """
        b = Base(100)
        self.assertEqual(b.id, 100)

    def test_init_with_neg_custom_id(self):
        """initialisation with one arg 
        (negative number)
        """
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_init_with_string_custom_id(self):
        """initialisation with one arg
        (string)
        """
        b = Base("holbies")
        self.assertEqual(b.id, "holbies")

    def test_init_with_char_custom_id(self):
        """initialisation with one arg
        (string 1 char)
        """
        b = Base('H')
        self.assertEqual(b.id, 'H')

    def test_init_with_float_custom_id(self):
        """initialisation with one arg
        (float)
        """
        b = Base(8.5)
        self.assertEqual(b.id, 8.5)

    def test_create_instance(self):
        """obj is instance of Base
        """
        obj = Base()
        self.assertIsInstance(obj, Base)

    def test_id_generation(self):
        """initialisation
        (no args)
        """
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string(self):
        obj = Base()
        json_str = obj.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_save_to_file(self):
        obj = Base()
        obj.save_to_file([])

    def test_from_json_string(self):
        json_str = '[]'
        obj_list = Base.from_json_string(json_str)
        self.assertEqual(obj_list, [])

    def test_load_from_file(self):
        pass

    def test_to_json_string_with_none(self):
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_from_json_string_with_none(self):
        obj_list = Base.from_json_string(None)
        self.assertEqual(obj_list, [])


if __name__ == '__main__':
    unittest.main()
