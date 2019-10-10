#!/usr/bin/python3
class LockedClass:
    """A locked class can't set attributes other
    than those mentioned as 'first_name'"""
    __slots__ = ['first_name']
