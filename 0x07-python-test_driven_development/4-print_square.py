#!/usr/bin/python3

""" This is print square module
    print a square with a given size
"""


def print_square(size):

    """ Size must be a integer, otherwise raise a error
    """
    # Size must be an integer
    if size < 0:
        raise ValueError("size must be >= 0")
        if type(size) is float:
            raise TypeError("size must be an integer")
    elif type(size) is not int:
        raise TypeError("size must be an integer")
    # Print square
    for row in range(size):
        for colum in range(size):
            # Print hashes
            print("#", end="")
        print()
