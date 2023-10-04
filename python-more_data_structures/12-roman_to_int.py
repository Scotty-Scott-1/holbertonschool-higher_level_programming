#!/usr/bin/python3
def roman_to_int(roman_string):

    if roman_string is None:
        return 0
    if not isinstance(roman_string, str):
        return 0

    my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 100}
    index = 0
    result = 0
    current = 0
    next = 0

    if len(roman_string) == 1:
        result = my_dict[roman_string[0]]
        return result

    for index in range(0, len(roman_string) - 1):

        current = my_dict[roman_string[index]]
        next = my_dict[roman_string[index + 1]]

        if current < next:
            result -= current
        else:
            result += current

    result += my_dict[roman_string[-1]]

    return result
