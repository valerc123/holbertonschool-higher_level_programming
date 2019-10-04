#!/usr/bin/python3


"""
This module said my name
"""


def say_my_name(first_name, last_name=""):
    """
    first_name and last_name must be a strings
    Returns: print my name
    """
    # if the parameters aren't string raise error
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    # Said my name
    print("My name is {} {}".format(first_name, last_name))
