#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    if len(my_list) < 1:
        return None

    new_list = my_list.copy()

    for i in my_list:
        if i % 2 == 0:
            new_list[i] = True
        elif i % 2 != 0:
            new_list[i] = False

    return new_list
