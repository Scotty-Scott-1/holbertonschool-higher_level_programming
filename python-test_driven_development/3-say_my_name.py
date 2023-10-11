#!/usr/bin/python3
"""
A function that error checks and then prints a first and/or last name
    first_name: a name
    last_name: a name
"""


def say_my_name(first_name, last_name=""):
    """a function that error checks and then prints a first and last name
    Return: None
    """
    if not first_name and last_name:
        return None

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("{} {}".format(first_name, last_name))
