#!usr/bin/python3
def remove_char_at(str, n):
    i = 0
    str_2 = ""

    while i < len(str):
        if i != n:
            str_2 += str[i]
        i += 1

    return str_2
