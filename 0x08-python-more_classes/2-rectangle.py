#!/usr/bin/python3
"""Module to import 2-rectangle
Defines a Rectangle
Private attributes and public area
"""


class Rectangle():
    """Defines a rectangle class with private attributes
    Args:
    width (int) : width
    height (int) : height
    Functions:
    __init__(self, width, height)
    width(self)
    width(self, value)
    height(self)
    height(self, value)
    area(self)
    perimeter(self)
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

    def area(self):
        """Return  area, width * height"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter, width*2 + height*2, or 0"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)