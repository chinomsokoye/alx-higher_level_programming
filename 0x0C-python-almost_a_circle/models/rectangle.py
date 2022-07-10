#!/usr/bin/python3
"""
Module rectangle
Defines, Creates a Rectangle class
Inherits from Base class
"""

import json
from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle class inheriting from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves width attribute"""
        return self.__width

    @property
    def height(self):
        """Retrieves height attribute"""
        return self.__height

    @property
    def x(self):
        """Retrieves x attribute"""
        return self.__x

    @property
    def y(self):
        """Retrieves y attributes"""
        return self.__y

    @width.setter
    def width(self, value):
        """Sets width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets x attributes"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets y attributes"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Computes area"""
        return self.__width * self.__height
