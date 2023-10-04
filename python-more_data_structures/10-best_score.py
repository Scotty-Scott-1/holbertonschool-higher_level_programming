#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is None:
        return

    best_name = ""
    highest_score = -1

    for name, score in a_dictionary.items():
        if score > highest_score:
            highest_score = score
            best_name = name

    return best_name
