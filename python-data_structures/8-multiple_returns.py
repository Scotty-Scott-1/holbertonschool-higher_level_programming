#!/usr/bin/python3
def multiple_returns(sentence):

    length = len(sentence)

    if len(sentence) < 1:
        first = None
    else:
        first = sentence[0]

    new_tuple = (length, first)

    return new_tuple
