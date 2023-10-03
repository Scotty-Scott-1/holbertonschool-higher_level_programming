#!/usr/bin/python3
def search_replace(my_list, search, replace):

    if len(my_list) < 1:
        return None

    new_list = []

    for element in my_list:
        if element != search:
            new_list.append(element)
        else:
            new_list.append(replace)

    return new_list
