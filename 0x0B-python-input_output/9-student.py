#!/usr/bin/python3
"""
Module 9-student
Class student that defines a student
"""


class Student:
    """Class student, defines student"""
    def __init__(self, first_name, last_name, age):
        """Inittializes the instance of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve dictionary representation of instance class"""
        return self.__dict__
