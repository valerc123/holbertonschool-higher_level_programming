#!/usr/bin/python3
"""Module containing Rectangle class"""


class Rectangle:
    """Class to create a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle with `width` and `height`.
        """
        self.__width = width
        self.__height = height

    # Private instance attribute: width
    @property
    def width(self):
        """Getter function for `width` attribute.
        Returns: value of `width` attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for `width` attribute.
        Args:
            value (int): value to use for `width`.
        Raises:
            TypeError: If `value` is not of type int.
            ValueError: If `value` is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # Private instance attribute: height
    @property
    def height(self):
        """Getter function for `height` attribute.
        Returns: value of `height` attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for `height` attribute.
        Args:
            value (int): value to use for `height`.
        Raises:
            TypeError: If `value` is not of type int.
            ValueError: If `value` is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        # Method to compute area of Rectangle instance
        area = self.__width * self.__height
        return area

    def perimeter(self):
        # Method to compute perimeter length of Rectangle instance.
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        perimeter = (self.__width + self.__height) * 2
        return perimeter
