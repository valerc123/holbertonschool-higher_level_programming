#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    # Private instance attribute: width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # Private instance attribute: height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        area = self.__width * self.__height
        return area

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        perimeter = (self.__width + self.__height) * 2
        return perimeter

    def __str__(self):
        new_str = ""
        if self.__width == 0 or self.__height == 0:
            return new_str
        for height in range(self.__height):
            for width in range(self.__width):
                new_str += "#"
            new_str += "\n"
        return new_str

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + "," + \
                str(self.__height) + ")"
