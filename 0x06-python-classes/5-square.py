#!/usr/bin/python3
"""
Module to import 5-square
Defines square class with private size and public area
Access and update size
Prints to stdout squares with #'s
"""


class Square:
    """Defines class square
    Args:
    size (int) : square size
    Functions:
    __init__(self, size)
    size(self)
    size(self, value)
    area(self)
    print(self)
    """
    def __init__(self, size=0)
    """Initialize square
    Attributes:
    size (int) : size of square, defaults to 0 if none
    """
    self.size = size

    @property
    def size(self):
        """
        Getter
        Returns: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter
        Args:
        value: sets size to value if int and >= 0
        """
        if type(valus) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes area of square
        Returns:
        area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints squares of #'s
        """
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
