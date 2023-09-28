#!/usr/bin/python3
import hidden_4


def print_names():
    if __name__ == "__main__":
        names = dir(hidden_4)
        sorted_names = sorted(name for name in names)
        for i in sorted_names:
            if not i.startswith("__"):
                print(i)


print_names()
