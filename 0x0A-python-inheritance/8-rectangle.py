#!/usr/bin/python3
"""Module 8-rectangle
Contains class Rectangle
"""


class BaseGeometry:
    """Defines the BaseGeometry class"""

    def area(self):
        """Raises Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validator for integer values"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""Rectangle class"""


class Rectangle(BaseGeometry):
    """Defines the Rectangle class"""
    def __init__(self, width, height):
        """Initializes Rectangle"""
        if super().integer_validator("width", width):
            self.__width = width
        if super().integer_validator("height", height):
            self.__height = height
