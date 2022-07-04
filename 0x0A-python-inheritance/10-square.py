#!/usr/bin/python3
"""Module 10-square
Contains a Square class created
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a class Square inherited from Rectangle"""
    def __init__(self, size):
        """Initializes the function for square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return string representation"""
        return super().__str__()

    def area(self):
        """Return computational value of area"""
        return self.__size ** 2
