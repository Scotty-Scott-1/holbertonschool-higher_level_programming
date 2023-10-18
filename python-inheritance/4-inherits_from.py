#!/usr/bin/python3
"""checks if obj is of a class that inherits"""


def inherits_from(obj, a_class):
    """checks is obj inherits"""
    if issubclass(type(obj), a_class):
        if type(obj) is not a_class:
            return True
    return False
