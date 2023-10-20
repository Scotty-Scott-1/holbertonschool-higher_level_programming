#!/usr/bin/python3
"""a module that returns a json dict of an obj"""


def class_to_json(obj):
    """A function that returns a json dict of an obj"""
    json_dict = {}

    if hasattr(obj, "__dict__"):
        json_dict = obj.__dict__.copy()
    return json_dict
