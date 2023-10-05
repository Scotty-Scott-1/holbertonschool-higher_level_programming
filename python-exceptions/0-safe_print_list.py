#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        j = 0

        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            if j <= x:
                j += 1

    except IndexError:
        print()
        return j

    print()
    return j
