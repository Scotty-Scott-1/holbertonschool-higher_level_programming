#!/usr/bin/python3
"""Write a class Student"""


class Student:

    def __init__(self, first_name, last_name, age):
        """initialize an instance of Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A function that returns a json dict of an obj"""
        json_dict = {}

        if hasattr(self, "__dict__"):
            json_dict = self.__dict__.copy()
        return json_dict
