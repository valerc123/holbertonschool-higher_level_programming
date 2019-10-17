#!/usr/bin/python3
'''
    My int module
'''


class MyInt(int):
    """Class My int inherits from int"""
    def __init__(self, n):
        """Initialitation values"""
        self.__n = n

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""
        return int(self) == other
