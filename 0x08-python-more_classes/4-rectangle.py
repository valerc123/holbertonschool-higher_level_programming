#!/usr/bin/python3
"""Module containing Rectangle class"""


class Rectangle:
    """Class to create a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle with `width` and `height`.
        Args:
            width (int): width of rectangle with value >= 0.
            height (int): height of rectangle with value >= 0.
        """
        self.width = width
        self.height = height

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
        """Method to compute area of Rectangle instance"""
        area = self.width * self.height
        return area

    def perimeter(self):
        """Method to compute perimeter length of Rectangle instance."""
        if self.width == 0 or self.height == 0:
            perimeter = 0
        perimeter = (self.width + self.height) * 2
        return perimeter

    def __str__(self):
        """Returns human readable string of """
        new_str = ""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            for height in range(self.height):
                for width in range(self.width):
                    new_str += "#"
                """Doesn't print the last line break"""
                if height != self.height - 1:
                     new_str += "\n"
        return new_str

    def __repr__(self):
        """Return: string representation of the rectangle"""
        return "Rectangle(" + str(self.width) + "," + \
                str(self.height) + ")"
