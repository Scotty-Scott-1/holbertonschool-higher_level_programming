#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    if len(matrix) < 1:
        return None

    new_matrix = []

    for row in matrix:
        new_row = list(map(get_sqaure, row))
        new_matrix.append(new_row)

    return new_matrix


def get_sqaure(num):
    return num * num
