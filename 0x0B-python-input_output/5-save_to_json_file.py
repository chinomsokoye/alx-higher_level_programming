#!/usr/bin/python3
"""
Module 5-save_to_json_file
Write an object to a text file
Using JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """Write JSON representation of an object to a text file"""
    with open(filename, 'w+') as files:
        json.dump(my_obj, files)
