#!/usr/bin/python3
"""a module that reads a file"""


def read_file(filename=""):
    """a function that reads from a file and prints. closes file"""
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read().rstrip()
        print(text, end="")
