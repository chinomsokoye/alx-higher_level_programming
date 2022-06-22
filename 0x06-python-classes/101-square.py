#!/usr/bin/python3
"""
Module import 101-square
Defines class square, private size, public area
Access and update size
Print to stdout #'s
"""


class Square:
    """Defines class square
    Args:
    size (int) : square size
    Functions:
    __init__(self, value, position)
    size(self)
    size(self, value)
    position(self)
    position(self, value)
    area(self)
    my_print(self)
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes square
        Attributes:
        size (int) : 0 or none
        position (int) : tiple of positive integer
        """
        self.size = size
        self.position = position

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
        value: sets size value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter
        Return: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter
        Args:
        value: set position to tuple of positive integers
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Computes area of square
        Returns:
        area
        """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)]))

    def __str__(self):
        """String representation of square print statement."""
        string = ""
        if self.__size == 0:
            return string

        string += "\n" * self.position[1]
        string += "\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)])
        return string
