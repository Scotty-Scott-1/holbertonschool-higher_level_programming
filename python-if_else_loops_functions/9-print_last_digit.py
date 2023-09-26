#!/usr/bin/python3

def print_last_digit(number):
    new_number = str(number)
    print("{}".format(new_number[-1]), end="")
    return int(new_number[-1])
