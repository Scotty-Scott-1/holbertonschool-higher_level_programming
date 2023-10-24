#!/usr/bin/python3
"""define a class Base"""
import json


class Base:
    """
    Class: Base

    Methods:
        __init__(self, id=None):
            initalize an instance of Base

        @staticmethod
        def to_json_string(list_dictionaries):
            converts an object to json string

        @classmethod
        def save_to_file(cls, list_objs):
            write a json string representation of list_objs to a json file

    Attributes:
        __nb_objects: count of instances of Base

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize an instance of base"""
        if id is None:
            self.id = Base.__nb_objects + 1
            Base.__nb_objects += 1
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """return a json representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) < 1:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write a json string representation of list_objs to a json file"""
        json_file = cls.__name__ + ".json"
        my_list = []

        if list_objs is not None:
            for obj in list_objs:
                my_list.append(obj.to_dictionary())
        with open(json_file, "w") as file:
            json.dump(my_list, file)
