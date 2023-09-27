#!/usr/bin/python3
def print_args():
    from sys import argv

    if __name__ == "__main__":

        if len(argv) == 1:
            print("{} arguments.".format(len(argv) - 1))

        elif len(argv) == 2:
            print("{} argument:".format(len(argv) - 1))
            print("1: {}".format(argv[1]))

        elif len(argv) > 2:
            print("{} arguments:".format(len(argv) - 1))
            for i in range(len(argv)):
                if i > 0:
                    print("{}: {}".format(i, argv[i]))


print_args()
