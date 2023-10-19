#!/usr/bin/python3
"""a module that appends a file"""


def append_write(filename="", text=""):
    """a function that appends to a file"""

    with open(filename, "a") as file:
        file.write(text)

    char_count = len(text)

    return char_count
