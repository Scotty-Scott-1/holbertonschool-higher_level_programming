#!/usr/bin/python3
"""Returns a list of methods and attributes"""


def lookup(obj):
    """lists all arrtribues and methods in obj(class)"""
    list = dir(obj)
    return list
