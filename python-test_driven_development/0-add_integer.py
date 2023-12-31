#!/usr/bin/python3
"""
A function that adds two ints after error checking
    a: an int or float
    b: an int of float
"""


def add_integer(a, b=98):
    """a function that error checks and adds 2 ints
    Return: sum of two ints
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    result = int(a) + int(b)

    return int(result)
