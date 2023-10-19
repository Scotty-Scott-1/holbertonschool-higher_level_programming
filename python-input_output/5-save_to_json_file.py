#!/usr/bin/python3
"""a module that appends a file"""


import json


def save_to_json_file(my_obj, filename):
    """a function a dumps and returns my obj"""
    json_rep = json.dumps(my_obj)
    with open(filename, "w") as file:
        file.write(json_rep)
