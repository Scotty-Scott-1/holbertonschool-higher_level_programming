#!/usr/bin/python3
""" A class with one privite instance attribute"""


class Square:
    """A class: sqaure that contains the a field for size

    Attributes:
        size: privite attr which describles ojbect's size
    """
    def __init__(self, size):
        self.__size = size
