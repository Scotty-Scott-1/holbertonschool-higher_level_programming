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

        @staticmethod
        def from_json_string(json_string):
            return a python list from json string

        @classmethod
        def create(cls, **dictionary):
            create an instance with values from dictionary(kwargs)

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
            file.write(Base.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """return a python list from json string"""
        new_list = []
        if json_string is None:
            return new_list

        if len(json_string) < 1:
            return new_list

        new_list = json.loads(json_string)
        return new_list

    @classmethod
    def create(cls, **dictionary):
        """create an instance with values from dictionary(kwargs)"""
        if dictionary:
            if len(dictionary) > 0:
                if cls.__name__ == "Rectangle":
                    new_instance = cls(5, 5)
                if cls.__name__ == "Sqaure":
                    new_instance = cls(5)

            new_instance.update(**dictionary)
        return new_instance
