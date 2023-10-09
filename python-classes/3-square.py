#!/usr/bin/python3
""" A class with one privite instance attribute and a public method"""


class Square:
    """A class: sqaure that contains the a field for size

    Attributes:
        size: privite attr which describles ojbect's size
    """
    def __init__(self, size=0):
        """instation of square object

        Args:
        size (int): size of the square

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ A method that returns the area of a sqaure object"""
        return self.__size * self.__size
