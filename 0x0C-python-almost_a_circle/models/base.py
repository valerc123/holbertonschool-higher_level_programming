#!/usr/bin/python3
"""
Module - Base
"""
import json
import turtle


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the Json string representation of list_dictionaries
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        filename = str(cls.__name__) + ".json"
        n_json = []

        with open(filename, 'w', encoding='utf-8') as f:
                if list_objs is None:
                    f.write("[]")
                else:
                    for obj in list_objs:
                        n_json.append(obj.to_dictionary())
                    f.write(cls.to_json_string(n_json))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        filename = cls.__name__ + ".json"
        list_instance = []

        try:
            with open(filename, "r", encoding="utf-8") as f:
                read_file = f.read()
                new_file = cls.from_json_string(read_file)
                for dic in new_file:
                    list_instance.append(cls.create(**dic))
                return list_instance
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        from random import randrange

        turtle.Screen().colormode(255)
        turt = turtle.Turtle()
        turt.color('blue')
        turt.pensize(5)
        turt.shape('turtle')

        for i in list_rectangles + list_squares:
            turt.penup()
            turt.setpos(i.x, i.y)
            turt.pendown()
            turt.color(randrange(255), randrange(255), randrange(255))
            turt.fillcolor(randrange(255), randrange(255), randrange(255))
            turt.begin_fill()
            turt.forward(i.width)
            turt.left(90)
            turt.forward(i.height)
            turt.left(90)
            turt.forward(i.width)
            turt.left(90)
            turt.forward(i.height)
            turt.left(90)
            turt.end_fill()
