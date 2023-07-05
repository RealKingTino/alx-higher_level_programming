#!/usr/bin/python3
"""

This module is composed by a function that divides the numbers of a matrix

"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): Matrix containing integers or floats.
        div (int or float): Number to divide the matrix elements by.

    Returns:
        list of lists: New matrix with elements divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats, or if each row of the matrix doesn't have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
def matrix_divided(matrix, div):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    
    return new_matrix
