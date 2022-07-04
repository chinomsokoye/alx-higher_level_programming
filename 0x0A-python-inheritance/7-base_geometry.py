#!/usr/bin/python3
"""Module 7-base_geometry
Contains BaseGeometry
Public method area, integer_validation
"""


class BaseGeometry:
    """Defines BaseGeometry class"""
    def area(self):
        """Raises Exception below"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validation for values"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
