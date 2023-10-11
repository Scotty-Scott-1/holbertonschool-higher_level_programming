#!/usr/bin/python3
"""
A function that divdes matrix by x after error checking
    matrix: a matrix contain int or floats. Rows same size
    div: number to divide matrix by
"""


def matrix_divided(matrix, div):
    """a function that error checks and divides matrix by div
    Return: new matrix
    """
    if not matrix:
        return None

    for row in matrix:
        for num in row:
            if not isinstance(num, int or float):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")

    row_length = len(matrix[0])

    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, int or float):
        raise TypeError("div must be a number")
    new_matrix = []

    for row in matrix:
        new_row = []
        for num in row:
            result = num / div
            rounded_result = round(result, 2)
            new_row.append(rounded_result)
        new_matrix.append(new_row)

    return new_matrix
