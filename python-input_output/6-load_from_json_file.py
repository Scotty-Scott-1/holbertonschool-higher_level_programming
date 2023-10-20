#!/usr/bin/python3
"""a module that creates an object from a json file"""

import json


def load_from_json_file(filename):
    """a function that creates an object from a json file"""
    with open(filename, "r", encoding="utf-8") as file:
        my_obj = json.load(file)
        return my_obj
