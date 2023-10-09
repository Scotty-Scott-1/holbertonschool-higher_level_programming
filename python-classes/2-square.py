#!/usr/bin/python3
""" A class with one privite instance attribute"""


class Square:
    """A class: sqaure that contains the a field for size

    Attributes:
        size: privite attr which describles ojbect's size
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
