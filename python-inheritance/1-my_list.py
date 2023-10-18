#!/usr/bin/python3
"""A module that defines a class"""


class MyList(list):
    """
    Mylist: A class that inherits the class list

    Methods:
        print_sorted: sorts self
    """

    def print_sorted(self):
        """A method that sorts and prints self"""
        print(sorted(self))
