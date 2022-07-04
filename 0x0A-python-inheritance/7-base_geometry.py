#!/usr/bin/python3
"""
Module 7-base_geometry
Contains BaseGeometry
Public instance method area, integer_validation
"""


class BaseGeometry:
    """Defines BaseGeometry class
    Methods:
    area(self)
    integer_validator(self, name, value)
    """
    def area(self):
        """Raises non implemented Exception below"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validation for integer values
        Args:
        name (str): name always a string
        value (int): greater than 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
