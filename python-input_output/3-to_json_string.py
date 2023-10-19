#!/usr/bin/python3
"""a module that appends a file"""


import json


def to_json_string(my_obj):
    """a function a dumps and returns my obj"""
    json_rep = json.dumps(my_obj)
    return json_rep
