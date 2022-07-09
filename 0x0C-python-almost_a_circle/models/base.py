#!/usr/bin/python3
"""
Module base
Defines Base class for classes in project
"""


import json
import os
import csv


class Base:
    """Defines a Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base instance class constructor"""
        if type(id) != int and id is not None:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
