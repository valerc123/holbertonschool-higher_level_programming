#!/usr/bin/python3
'''
Module - inherits_from
'''


def inherits_from(obj, a_class):
    '''Function that returns True if the object is an instance
      of a class that inherited (directly or indirectly) from
      the specified class ; otherwise False.
    '''
    if isinstance(obj, a_class) is True and type(obj) is not a_class:
        return True
    else:
        return False
