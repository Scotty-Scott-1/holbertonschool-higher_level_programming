#!/usr/bin/python3
"""A module that defines a class"""


class MyList(list):
    """Mylist: A class that inherits the class list
        Methods: print_sorted(self): sorts self
    """

    def print_sorted(self):
        """print list in order"""
        print(sorted(self))
