#!/usr/bin/python3
"""define a class Base"""


class Base:
    """
    Class: Base

    Methods:
         __init__(self, id=None): initalize an instance of Base

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
