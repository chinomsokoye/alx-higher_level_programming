#!/usr/bin/python3
"""
Module 8-class_to_json.py
Returns dictionary description with simple data structure
JSON serialization of object
"""


def class_to_json(obj):
    """Creates dictionary representation of object"""
    return obj.__dict__
