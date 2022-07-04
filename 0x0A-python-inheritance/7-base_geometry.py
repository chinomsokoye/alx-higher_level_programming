#!/usr/bin/python3
"""
Module 7-base_geometry
Creates a BaseGeometry class
"""


class BaseGeometry:
    """Defines and create BaseGeometry class"""
    def area(self):
        """Raise Exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Function for validation of integer values"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
