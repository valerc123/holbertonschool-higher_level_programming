#!/usr/bin/python3
"""Module implementing LockedClass class.
    LockedClass is a class that uses the __slots__ attribute to prevent
    dynamic attribute creation.
"""


class LockedClass:
    """A locked class can't set attributes other
    than those mentioned as 'first_name'"""
    __slots__ = ['first_name']
