#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    '''Class Rectangle that inherits from class Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getters of width """
        return self.__width

    @width.setter
    def width(self, value):
        """Setters of width """
        self.__width = value

    @property
    def height(self):
        """Getters of height """
        return self.__height

    @height.setter
    def height(self, value):
        """Setters of height """
        self.__height = value

    @property
    def x(self):
        """Getters of x """
        return self.__x

    @x.setter
    def x(self, value):
        """Setters of x """
        self.__x = value

    @property
    def y(self):
        """Getters of y """
        return self.__y

    @y.setter
    def y(self, value):
        """Setters of y """
        self.__y = value
