#!/usr/bin/python3
"""
Module import 102-square
Defines class square, private size, public area
Access and update size
"""


class Square:
    """Defines square class
    Args:
    size (int) : square size
    Functions:
    __init__(self, size)
    size(self)
    size(self, value)
    area(self)
    """
    def __init__(self, size=0):
        """Initializes square
        Attributes:
        size (int) : 0 or none
        """
        self.size = size

    @property
    def size(self):
        """
        Getter
        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter
        Args:
        value: set size to value
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

    def __eq__(self, other):
        """Returns equality."""
        return self.size == other.size

    def __ne__(self, other):
        """Returns inequality."""
        return self.size != other.size

    def __lt__(self, other):
        """Returns less than."""
        return self.size < other.size

    def __le__(self, other):
        """Returns less than or equal to."""
        return self.size <= other.size

    def __gt__(self, other):
        """Returns greater than."""
        return self.size > other.size

    def __ge__(self, other):
        """Returns greater than or equal to."""
        return self.size >= other.size
