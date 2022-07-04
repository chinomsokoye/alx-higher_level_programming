#!/usr/bin/python3
"""
Module 101-add_attribute
Check to add attribute to object
"""


def add_attribute(an_obj, an_attr, a_value):
    """Checks if attribute of a value can be added to object"""
    if ('__dict__' in dir(an_obj)):
        setattr(an_obj, an_attr, a_value)
    else:
        raise TypeError("can't add new attribute")
