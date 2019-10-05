#!/usr/bin/python3
"""
    add_integer module:
	contains a fuction that adds to integers
"""


def add_integer(a, b=98):

    """
	adds two integers
    Parameters
    ----------
    a : int or float
    b : int or float
    Returns
    -------
    Returns an integer: the addition of a and b
    """

	# Cast the variables if are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    # The variables must be integers
    if not (isinstance(a, int)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int)):
        raise TypeError("b must be an integer")
    return a + b
