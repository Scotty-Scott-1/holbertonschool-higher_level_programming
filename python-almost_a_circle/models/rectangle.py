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

        def width(self, value):
            setter for width

        def height(self, value):
            setter fir height

        def x(self, value):
            setter for x

         def x(self, value):
            setter for y

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

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be > 0")

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be > 0")

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
        """error checks and updates width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """error checks and updates height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """error checks and updates x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """error checks and updates y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")

        self.__y = value
