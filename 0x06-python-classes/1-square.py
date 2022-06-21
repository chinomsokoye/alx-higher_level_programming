#!/usr/bin/python3
"""
Module to import 1-square
Defines a square with a private attribute size
"""


class Square:
    """Represents a square
    Args:
    size : size of square side
    """
    def __init__(self, size):
        """Initializes a square
        Attributes:
        size : square size
        """
        self.__size = size
