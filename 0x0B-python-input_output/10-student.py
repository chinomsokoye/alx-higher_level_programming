#!/usr/bin/python3
"""
Module 10-student
Class student that defines a student
"""


class Student:
    """Class student, defines student"""
    def __init__(self, first_name, last_name, age):
        """Inittializes the instance of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of instance class"""
        my_dict = dict()
        if type(attrs) is list and all(type(i) is str for i in attrs):
            for i in attrs:
                if i in self.__dict__:
                    my_dict.update({i: self.__dict__[i]})
            return my_dict
        return self.__dict__.copy()
