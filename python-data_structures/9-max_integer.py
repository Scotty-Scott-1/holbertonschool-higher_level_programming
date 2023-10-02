#!/usr/bin/python3
def max_integer(my_list=[]):
    result = 0

    if len(my_list) < 1:
        return None

    if len(my_list) == 1:
        return my_list[0]

    result = my_list[0]

    for i in my_list:
        if result < i:
            result = i

    return result
