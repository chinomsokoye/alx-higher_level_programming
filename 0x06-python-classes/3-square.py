#!/usr/bin/python3
"""
Module to import 3-square
Defines square with private attribute size and public attribute area
"""


class Square:
    """Represents class square
    Args:
    size (int) : square size
    Functions:
    __init__(self, size)
    area(self)
    """
    def __init__(self, size=0):
        """Initializes square
        Attributes:
        __size (int) : square size, 0 if none
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Computes area of square
        Returns:
        area
        """
        return self.__size ** 2
