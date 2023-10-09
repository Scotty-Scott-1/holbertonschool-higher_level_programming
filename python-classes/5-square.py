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
        size (int): size of the square. Called and set by setter and getter
        """
        self.__size = size

    @property
    def size(self):
        """A getter method for calling the value of object.__size"""
        return self.__size

    @size.setter
    def size(self, value):
        """A setter method for setting value of object.__size

        Args:
        value: the value to be checked for errors then set as object__size

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ A method that returns the area of a sqaure object"""
        return self.__size * self.__size

    def my_print(self):
        """A method that prints the the sqaure according to size"""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
