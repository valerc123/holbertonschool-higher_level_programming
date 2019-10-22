#!/usr/bin/python3
"""Imports module Base"""
from models.base import Base


class Rectangle(Base):
    '''Class Rectangle that inherits from class Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialitation of attributes"""
        super().__init__(id)
        """Call super class with id"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getters of width """
        return self.__width

    @width.setter
    def width(self, value):
        """Setters of width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getters of height """
        return self.__height

    @height.setter
    def height(self, value):
        """Setters of height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getters of x """
        return self.__x

    @x.setter
    def x(self, value):
        """Setters of x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getters of y """
        return self.__y

    @y.setter
    def y(self, value):
        """Setters of y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area value of the Rectangle instance """
        return self.height * self.width

    def display(self):
        """Print a rectangle display"""
        spaces = self.x
        n_line = self.y
        if n_line != 0:
            print('\n' * (n_line - 1))
        for j in range(self.height):
            print(" "*spaces + '#'*self.width)

    def __str__(self):
        "Informal rectangle string representation"
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.x,
                                                                 self.y,
                                                                 self.width,
                                                                 self.height)

    def update(self, *args, **kwargs):
        """
        Update method: update the dictionary (key/value)
        argument to each attribute

        Args:
           args: single pointer to a dictionary: key/value
           kwargs: dictionary with key/value arguments
        """
        if args and len(args) > 0:
            for index, arg in enumerate(args):
                if index == 0:
                   # super().__init__(arg)\
                    self.id = arg
                if index == 1:
                    self.width = arg
                if index == 2:
                    self.height = arg
                if index == 3:
                    self.x = arg
                if index == 4:
                    self.y = arg
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of Rectangle"""
        attr = ['id', 'width', 'height', 'x', 'y']
        return {key: getattr(self, key) for key in attr}
