#!/usr/bin/python3
"""define a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class: Square
        Parent: Rectangle

    Methods:
        __init__(self, size, x=0, y=0, id=None):
            initalize an instance of Square

        __str__(self):
            [Square] (<id>) <x>/<y> - <size>

        def update(self, *args, **kwargs):
            updates attrs with a variable number of args

    Attributes:
        self.id: inherited from parent
        self.x: inherited from parent
        self.y: inherited from parent
        self.width: inherited from parent
        self.height: inherited from parent

    """
    def __init__(self, size, x=0, y=0, id=None):
        """initialize an intance of Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """[Square] (<id>) <x>/<y> - <size>"""
        return (
            "[Square] ({}) {}/{} - {}"
            .format(self.id, self.x, self.y, self.height)
            )

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates attrs with a variable number of args"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Prints a dictionary representation of Sqaure instance"""
        my_dict = {
                    "id": self.id,
                    "x": self.x,
                    "size": self.width,
                    "y": self.y,
                    }
        return my_dict
