#!/usr/bin/python3
import json


class Base:
    __nb_objects = 0
    """Base class"""
    def __init__(self, id=None):
        """Initialize the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Returns the Json string representation of list_dictionaries"""
        if list_dictionaries is None or []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
