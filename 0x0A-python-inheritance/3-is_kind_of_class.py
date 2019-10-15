#!/usr/bin/python3
"""Module that verify if the object is an instances of a class given
"""


def is_kind_of_class(obj, a_class):
    """ Function that receive an object and a class,
        Returns true if object is an instances of a class,
        otherwise return false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
