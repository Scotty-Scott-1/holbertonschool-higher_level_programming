#!/usr/bin/python3
"""a module that returns a json dict of an obj"""


import json


def class_to_json(obj):
    """A function that returns a json dict of an obj"""
    json_dict = json.dumps(obj.__dict__)
    return json_dict
