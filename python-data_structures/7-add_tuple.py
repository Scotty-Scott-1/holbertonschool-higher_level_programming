#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = (0, 0)
    element_a_0 = 0
    element_a_1 = 0
    element_b_0 = 0
    element_b_1 = 0

    if len(tuple_a) < 1 and len(tuple_b) < 0:
        return new_tuple

    if len(tuple_a) > 0:
        element_a_0 = tuple_a[0]

    if len(tuple_b) > 0:
        element_b_0 = tuple_b[0]

    if len(tuple_a) > 1:
        element_a_1 = tuple_a[1]

    if len(tuple_b) > 1:
        element_b_1 = tuple_b[1]

    new_tuple = (element_a_0 + element_b_0, element_a_1 + element_b_1)
    return new_tuple
