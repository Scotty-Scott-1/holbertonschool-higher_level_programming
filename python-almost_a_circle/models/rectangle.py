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

        def __str__(self):
            prints info: [Rectangle] (<id>) <x>/<y> - <width>/<height>

        def update(self, *args):
            updates attrs with a variable number of args
            index: 0: id, 1: width, 2: height, 3: x, 4: y

        def display(self):
            prints the object in #s. takes into account x and y possition

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
            raise ValueError("x must be >= 0")

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

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
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """error checks and updates y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """returns the area of the object"""
        return self.__height * self.__width

    def display(self):
        """prints the object in #s. takes into account x and y possition"""
        for num in range(self.__y):
            print()
        for i in range(self.__height):
            for i in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """[Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return (
            "[Rectangle] ({}) {}/{} - {}/{}"
            .format(self.id, self.__x, self.__y, self.__width, self.__height)
            )

    def update(self, *args, **kwargs):
        """updates attrs with a variable number of args"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]

    def to_dictionary(self):
        my_dict = {
                    "x": self.__x, "y": self.__y, "id": self.id,
                    "height": self.__height, "width": self.__width
                    }
        return my_dict
