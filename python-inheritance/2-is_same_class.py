#!/usr/bin/python3
"""a function that check for if obj is class"""


def is_same_class(obj, a_class):
    """check if object is class"""
    if type(obj) is a_class:
        return True
    else:
        return False
