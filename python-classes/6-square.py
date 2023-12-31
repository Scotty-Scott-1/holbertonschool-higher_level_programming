#!/usr/bin/python3
""" A class with one privite instance attribute and a public method"""


class Square:
    """A class: sqaure that contains the a field for size

    Attributes:
        size: privite attr which describles ojbect's size
    """
    def __init__(self, size=0, position=(0, 0)):
        """instation of square object

        Args:
        size (int): size of the square. Called and set by setter and getter
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if (
            not isinstance(position, tuple)
            or len(position) != 2
            or not isinstance(position[0], int)
            or not isinstance(position[1], int)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ A method that returns the area of a sqaure object"""
        return self.__size * self.__size

    def my_print(self):
        """Method that prints the the sqaure according to size and position"""
        if self.size == 0:
            print()
        else:
            num = self.position[1]
            for y in range(self.position[1]):
                print()
            for i in range(self.size):
                for x in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()
