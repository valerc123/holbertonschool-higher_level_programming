#!/usr/bin/python3
"""
    Module - MyList class
"""


class MyList(list):
    """
    Derived class Mylist
    inherits from the class list
    """

    def print_sorted(self):
        """
        Function that returns a list sorted
        """
        print(sorted(self))
