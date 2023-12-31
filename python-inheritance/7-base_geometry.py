#!/usr/bin/python3
"""Write a class"""


class BaseGeometry:
    """
    Class: BaseGeometry

    Methods:
        area: raises an error
        integer_validator: checks if value is valid
    """

    def area(self):
        """raises an error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if value is valid"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
