#!/usr/bin/python3
"""
Module to import 2-square
Defines a square with private attribute size, validates size
"""


class Square:
    """Class square
    Args:
    size (int) : size of square
    """
    def __init__(self, size=0):
        """Initializes square
        Attributes:
        __size (int) : square size, defaults to 0 if none
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
