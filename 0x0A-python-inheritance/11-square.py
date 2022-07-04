#!/usr/bin/python3
"""
Module 11-square
Contains class to create a square
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a Square class
    Inherits from Rectangle
    """
    def __init__(self, size):
        """Initializes a Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns string representation"""
        return str("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Returns computational area of Square class"""
        return self.__size ** 2
