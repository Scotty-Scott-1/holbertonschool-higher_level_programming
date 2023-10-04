#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is None or a_dictionary == []:
        return None

    result = max(a_dictionary, key=a_dictionary.get)

    if a_dictionary[result] == 0:
        return None

    return result
