#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    try:
        j = 0

        for i in range(0, x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                if j <= x:
                    j += 1

    except (ValueError, TypeError):
        print()
        return j

    print()
    return j
