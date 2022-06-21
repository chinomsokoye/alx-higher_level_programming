#!/usr/bin/python3
"""
Module to import 4-square
Defines square with private size and public area
Can access update
"""


class Square:
    """Represents square
    Args:
    size (int) : square size
    Functions:
    __init(self, size)
    size(self)
    size(self, value)
    area(self)
    """
    def __init__(self, size=0):
        """Initialize square
        Attributes:
        size (int) : square size, 0 if none
        """
        self.size = size

    @property
    def size(self):
        """Defines getter
        Returns: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Defines setter
        Args:
        value : sets size to value, if int and >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Computes area of square
        Returns:
        area
        """
        return self.__size ** 2
