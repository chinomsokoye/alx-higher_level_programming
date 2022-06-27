#!/usr/bin/python3
"""Module to import 1-rectangle
Defines a Rectangle
"""


class Rectangle():
    """Defines a rectangle class
    Args:
    width (int) : width
    height (int) : height
    Functions:
    __init__(self, width, height)
    width(self)
    width(self, value)
    height(self)
    height(self, value)
    """
    def __init__(self, width=0, height=0):
        """Initializes rectangles"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter to width if int > 0"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter to height if int > 0"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
