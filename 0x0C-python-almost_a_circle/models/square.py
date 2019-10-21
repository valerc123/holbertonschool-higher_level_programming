#!/usr/bin/python3
"""Imports module rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Representation of a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        "Informal Square string representation"
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.size)

    @property
    def size(self):
        """Getter: get size of square
        Return: size of square
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter: set argument value to size
        Args:
            value: size of squre
        """
        self.width = value
        self.height = value
