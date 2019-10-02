#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

        if not isinstance(self.__position, tuple) \
           or len(self.__position) != 2 \
           or not isinstance(self.__position[0], int) \
           or not isinstance(self.__position[1], int) \
           or (self.__position[0] < 0) or (self.__position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(self.__position) != 2 \
           or not isinstance(value[0], int) or not isinstance(value[1], int) \
           or (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        area = self.__size ** 2
        return area

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for spaces in range(self.__position[1]):
            print()
        for row in range(self.__size):
            for colum in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("{}".format("#"), end="")
            print()
