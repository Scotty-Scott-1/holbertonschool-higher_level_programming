#!/usr/bin/python3
"""return a matrix of pascals triangle"""


def pascal_triangle(n):
    """return a matrix of pascals triangle"""
    tri = []

    if n <= 0:
        return tri

    for i in range(n):
        if i == 0:
            row = [1]
        else:
            prev_row = tri[-1]
            row = [1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
        tri.append(row)

    return tri
