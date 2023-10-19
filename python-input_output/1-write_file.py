#!/usr/bin/python3
"""a module that reads a file"""


def write_file(filename="", text=""):
    """a function that writes ()overwrites to a file"""

    with open(filename, "w") as file:
        file.write(text)

    char_count = len(text)

    return char_count
