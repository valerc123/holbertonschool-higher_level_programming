#!/usr/bin/python3

"""
This is the divide module.
has a function to divide matrix
Divide all elements of a matrix
"""


def matrix_divided(matrix, div):

    """
    matrix must be a list of lists of integers/floats
    Returns a new matrix
    """
    new_matrix = []
    length = 0
    # div can't be  0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # if the divisor is neither integer nor float
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    # Matrix must be a list of integers or floats
    if matrix == [] or matrix == [[]]:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if not isinstance(matrix[0], list) or not isinstance(matrix[1], list):
            raise TypeError('matrix must be a matrix (list of lists) '
                            'of integers/floats')
    # matrix has to exist, can't be less or equal to 0
    if len(matrix[0]) <= 0:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')

    # 1. Let's create new matrix with new_row
    for row in matrix:
        # Create new_row
        new_row = []
        # matrix must be a list
        if type(matrix) is not list:
            raise TypeError('matrix must be a matrix (list of lists)  '
                            'of integers/floats')
    # 2. Row is empty
        if length == 0:
            length = len(row)
        # Each row must be the same size, TypeError
        elif len(row) is not length:
            raise TypeError('Each row of the matrix must have the same size')
    # 3. Each item must be an integer or float
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) '
                                'of integers/floats')
    # 4. add content to the row
        # All elements will be divided by div and rounded to 2 decimal places.
            new_row.append(round((item / div), 2))
        # Add content to the matrix
        new_matrix.append(new_row)
    return new_matrix
