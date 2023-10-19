#!/usr/bin/python3
"""Write a class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class: Rectangle

    Methods:
        __init__(self, width, height): initialized rectangle
        area(self): returns area of rectangle
        __str__(self): prints some info about rectangle
    """

    def __init__(self, width, height):
        """initialises rectangle"""
        self.__height = height
        self.__width = width
        self.integer_validator("height", height)
        self.integer_validator("width", width)

    def area(self):
        """returns area"""
        return self.__height * self.__width

    def __str__(self):
        """prints some info"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
