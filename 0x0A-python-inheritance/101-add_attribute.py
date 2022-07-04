#!/usr/bin/python3
"""
Module 101-add_attribute
Check to add attribute to object
"""


def add_attribute(an_obj, an_attr, a_value):
    """Checks if attribute of a value can be added to object"""
    if not hasattr(an_obj, '__slots__') and not hasattr(an_obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if not hasattr(an_obj, '__slots__') and not hasattr(an_obj, an_attr):
        raise TypeError("can't add new attribute")
    setattr(an_obj, an_attr, a_value)
