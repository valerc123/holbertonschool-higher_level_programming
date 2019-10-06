#!/usr/bin/python3


"""
matrix_divided module:
contains a function that divides all elements in a matrix
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    Parameters
    ----------
    matrix : list
        list of lists that contains int or floats (2-dimensional list)
    div : int or float
        number to divide elements by
    Returns
    -------
    list
        a new matrix with elements that have been divided by div
    """

    # matrix should be a list of lists
    err = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(matrix) is not list:
        raise TypeError(err)
    for row in matrix:
        if type(row) is not list:
            raise TypeError(err)

    # make sure div is not 0
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')

    # make sure each element is an int or float
    for row in matrix:
        for elem in row:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError(err)

    # make sure all rows are the same size
    length_of_rows = []
    for row in matrix:
        length_of_rows.append(len(row))
    length_of_rows = set(length_of_rows)
    if len(length_of_rows) > 1:
        raise TypeError('Each row of the matrix must have the same size')

    # finally, do the division and return the new matrix
    new_matrix = []
    for row in matrix:
        new_matrix.append([round((x/div), 2) for x in row])
    return new_matrix
