#!/usr/bin/python3
"""
Module to import 0-add_integer
Function to add two integer sum
Accepts values, returns sum
"""


def add_integer(a, b=98):
    """Return integer sum of a and b"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
