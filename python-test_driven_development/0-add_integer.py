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
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(b, float):
        b = int(b)
    if isinstance(a, float):
        a = int(a)

    return a + b
