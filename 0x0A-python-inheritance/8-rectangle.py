#!/usr/bin/python3
"""Module 8-rectangle
Contains class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines class rectangle
    Inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """Initializes class instance
        Arguments allowed
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
