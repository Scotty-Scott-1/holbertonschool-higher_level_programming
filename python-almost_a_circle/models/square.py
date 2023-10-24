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
