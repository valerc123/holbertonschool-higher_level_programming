#!/usr/bin/python3
"""Module that return True if the object
   is instance of specified class
"""


def is_same_class(obj, a_class):
    """Fuction that validates if the object is the
       same type as the class, if they are not equal return false
    """
    if type(obj) is a_class:
        return True
    else:
        return False
