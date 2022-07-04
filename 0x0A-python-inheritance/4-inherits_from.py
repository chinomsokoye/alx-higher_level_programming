#!/usr/bin/python3
"""Module 4-inherits_from
Contains method
Returns True if class is inherited
"""


def inherits_from(obj, a_class):
    """Defines method of function"""
    if type(obj) == a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
