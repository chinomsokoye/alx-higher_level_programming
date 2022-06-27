#!/usr/bin/python3
"""Module to import 8-rectangle
Defines a Rectangle
Private attributes and public area, prints any given symbol, deletes
Keep track of instances using public attributes
Static methods returns bigger rectangle of given two
"""


class Rectangle():
    """Defines a rectangle class with private attributes
    Args:
    width (int) : width
    height (int) : height
    Functions:
    __init__(self, width, height)
    width(self)
    width(self, value)
    height(self)
    height(self, value)
    area(self)
    perimeter(self)
    __str__(self)
    __repr__(self)
    __del__(self)
    bigger_or_equal(rect_1, rect_2)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes rectangles"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """Deletes an instance of a class"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        """Getter returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter to width if int > 0"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter to height if int > 0"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return  area, width * height"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter, width*2 + height*2, or 0"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """Prints rectangle #'s unofficially"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = "\n".join([str(self.print_symbol) * self.__width
                         for rows in range(self.__height)])
        return rec

    def __repr__(self):
        """String representation to create a new instance"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
