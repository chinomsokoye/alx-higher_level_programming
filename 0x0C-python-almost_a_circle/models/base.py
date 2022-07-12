#!/usr/bin/python3
"""
Module base
Defines Base class for classes in project
"""


import json
import os
import csv


class Base:
    """Defines a Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base instance class constructor"""
        if type(id) != int and id is not None:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or
            not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to a file"""
        if list_objs is None or list_objs == []:
            jst = "[]"
        else:
            jst = cls.to_json_string([i.to_dictionary() for i in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as files:
            files.write(jst)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of JSON string representation of json_string"""
        ls = []
        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            ls = json.loads(json_string)
        return ls

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set already"""
        if cls.__name__ == 'Rectangle':
            exm = cls(1, 1)
        elif cls.__name__ == 'Square':
            exm = cls(1)
        exm.update(**dictionary)
        return exm

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        ls = []
        list_dicts = []
        if os.path.exists(filename):
            with open(filename, 'r') as files:
                st = files.read()
                list_dicts = cls.from_json_string(st)
                for ds in list_dicts:
                    ls.append(cls.create(**ds))
        return ls

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list_objs in csv format to a file"""
        if (type(list_objs) != list and
            list_objs is not None or
            not all(isinstance(x, cls) for x in list_objs)):
            raise TypeError("list_objs must be a list of instances")
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as files:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                    writer = csv.DictWriter(files, fieldnames=fields)
                    writer.writeheader()
                    writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize CSV from a file"""
        filename = cls.__name__ + ".csv"
        ls = []
        if os.path.exists(filename):
            with open(filename, 'r') as files:
                reader = csv.reader(files, delimiter=',')
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                for x, row in enumerate(reader):
                    if x > 0:
                        i = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(i, fields[j], int(e))
                        ls.append(i)
        return ls

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Turtle graphics draw rectangles and squares"""
        import turtle
        import time
        from random import randrange

        amy = turtle.Turtle()
        amy.color("red")
        turtle.bgcolor("green")
        amy.shape("square")
        amy.pensize(6)

        for i in (list_rectangles + list_squares):
            amy.penup()
            amy.setpos(0, 0)
            turtle.Screen().colormode(255)
            amy.pencolor((randrange(255), randrange(255), randrange(255)))
            Base.draw_rect(amy, i)
            time.sleep(2)
        time.sleep(4)

    @staticmethod
    def draw_rect(amy, rect):
        """Draws a Rectangle or Square"""
        amy.penup()
        amy.setpos(rect.x, rect.y)
        amy.pendown()
        amy.forward(rect.width)
        amy.left(90)
        amy.forward(rect.height)
        amy.left(90)
        amy.forward(rect.width)
        amy.left(90)
        amy.forward(rect.height)
