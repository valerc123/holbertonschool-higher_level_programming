#!/usr/bin/python3
"""Module that contain List
"""


class MyList(list):
    """The elements of the list is interger,
    returns the list sorted """

    def print_sorted(self):
        """Function that returns a list sorted"""
        print(sorted(self))