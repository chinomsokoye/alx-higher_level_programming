#!/usr/bin/python3
"""Module 9-rectangle
Contains class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines the class Rectangle
    Inheriting from BaseGeometry
    """
    def __init__(self, width, height):
        """Initializes a class instance __init__"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns string representation formatted"""
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """Returns the computational area of the Rectangle"""
        return self.__width * self.__height
