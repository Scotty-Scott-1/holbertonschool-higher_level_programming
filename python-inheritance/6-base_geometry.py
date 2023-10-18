#!/usr/bin/python3
"""Write a class"""


class BaseGeometry:
    """
    Class: BaseGeometry

    Methods:
        area: raises an error
    """
    def area(self):
        """raises an error"""
        raise Exception("area() is not implemented")
