#!/usr/bin/python3
"""
    Module - Square
"""

from models.rectangle import Rectangle

""" Imports module rectangle """


class Square(Rectangle):
    """ Representation of a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Informal Square string representation"""
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

    def update(self, *args, **kwargs):
        """Update method: update the dictionary (key/value)
        argument to each attribute
        Args:
            args: single pointer to a dictionary: key/value
            kwargs: dictionary with key/value arguments
        """

        if args and len(args) > 0:
            for index, arg in enumerate(args):
                if index == 0:
                   # super().__init__(arg)
                    self.id = arg
                if index == 1:
                    self.size = arg
                if index == 2:
                    self.x = arg
                if index == 3:
                    self.y = arg
        elif kwargs and kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of Square
        """
        attr = ['id', 'size', 'x', 'y']
        return {key: getattr(self, key) for key in attr}
