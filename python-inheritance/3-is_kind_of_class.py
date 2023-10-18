#!/usr/bin/python3
"""a function that check for if obj is isntance a class
or instance subclass or a_class"""


def is_kind_of_class(obj, a_class):
    """checks if obj is an instance of a_class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
