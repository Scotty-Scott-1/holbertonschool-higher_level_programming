#!/usr/bin/python3
"""Write a class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class: Rectangle

    Methods:
        __init__(self, width, height): initialized rectangle
    """

    def __init__(self, width, height):
        """initialises rectangle"""
        self.__height = height
        self.__width = width
        self.integer_validator("height", height)
        self.integer_validator("width", width)
