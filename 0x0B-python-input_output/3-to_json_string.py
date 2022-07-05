#!/usr/bin/python3
"""
Module 3-to_json_string
Return JSON representation of a string object
"""


import json


def to_json_string(my_obj):
    """Returns JSON representation of s string object"""
    return json.dumps(my_obj)
