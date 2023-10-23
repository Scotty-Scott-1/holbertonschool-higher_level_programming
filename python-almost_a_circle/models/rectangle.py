#!/usr/bin/python3
"""define a class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """
    Class: Reactangle
        Parent: Base

    Methods:
         __init__(self, width, height, x=0, y=0, id=None):
            initalize an instance of Rectangle

    Attributes:
         super().__init__(id)
        self.__width: width of rectangle
        self.__height: height of rectangle
        self.__x: x position of rectangle
        self.__y: y position of rectangle

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize a rectanlge innstance"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value
