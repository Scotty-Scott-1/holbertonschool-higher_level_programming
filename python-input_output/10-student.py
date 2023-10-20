#!/usr/bin/python3
"""Write a class Student"""


class Student:

    def __init__(self, first_name, last_name, age):
        """initialize an instance of Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A function that returns a json dict of an obj"""
        json_dict = {}

        if attrs is None:
            attrs = self.__dict__.keys()

        for atts in attrs:
            if hasattr(self, atts):
                json_dict[atts] = getattr(self, atts)

        key_order = ["age", "last_name", "first_name"]

        new_json_dict = {}
        for key in key_order:
            if key in json_dict:
                new_json_dict[key] = json_dict[key]

        return new_json_dict
