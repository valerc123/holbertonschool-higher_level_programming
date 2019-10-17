#!/usr/bin/python3
'''
Rectangle module
'''
base_geometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(base_geometry):
    """A representation of a rectangle"""

    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates the area"""
        return self.__width * self.__height

    def __str__(self):
        """Informal string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
