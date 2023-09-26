#!/usr/bin/python3
def uppercase(str):
    str2 = ""

    for i in str:
        if i >= 'a':
            if i <= 'z':
                str2 += chr(ord(i) - ord('a') + ord('A'))
        else:
            str2 += i

    print("{}".format(str2))
