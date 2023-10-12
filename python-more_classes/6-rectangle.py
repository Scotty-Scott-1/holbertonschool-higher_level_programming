#!/usr/bin/python3
"""A class that defines a rectangles"""


class Rectangle:
    """A Rectange class
    Attributes:
        height: private
        width: private
    """

    number_of_instances = 0
    def __init__(self, width=0, height=0):

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """A method that returns the area of object"""
        return self.__width * self.__height

    def perimeter(self):
        """A method that returns the perimeter of object"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return self.__height + self.__height + self.__width + self.__width

    def __str__(self):

        new_string = ""

        if self.height == 0 or self.width == 0:
            return new_string

        for i in range(self.height):
            for j in range(self.width):
                new_string += "#"
            if i < self.height - 1:
                new_string += "\n"

        return new_string

    def __repr__(self):
        new_string = "Rectangle({}, {})".format(self.width, self.height)
        return new_string

    def __del__(self):

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

        return
