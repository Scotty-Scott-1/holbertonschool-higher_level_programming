#!/usr/bin/python3
"""Write a class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class: Square

    Methods:
        __init__(self, width, height): initialized rectangle
        area(self): returns area
        def __str__(self): prints some info

    Attributes:
        __size: private attr for size
    """

    def __init__(self, size):
        """initialises a square instance"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns area"""
        return self.__size * self.__size

    def __str__(self):
        """returns some info"""
        return "[Square] {}/{}".format(self.__size, self.__size)
