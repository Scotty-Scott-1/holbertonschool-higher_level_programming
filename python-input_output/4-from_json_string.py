#!/usr/bin/python3
"""a module that convets a file to python data structure from json"""


import json


def from_json_string(my_str):
    """ a function that converted to python data structure from json"""
    py_data = json.loads(my_str)
    return py_data
