#!/usr/bin/python3
"""a module that appends a file"""


import json


def save_to_json_file(my_obj, filename):
    """a function a dumps and returns my obj"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
