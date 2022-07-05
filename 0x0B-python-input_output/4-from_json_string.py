#!/usr/bin/python3
"""
Module 4-from_json_string
Returns an object represented by JSON string
Python Data Structures
"""


import json


def from_json_string(my_str):
    """Return object representation of JSON string"""
    return json.loads(my_str)
