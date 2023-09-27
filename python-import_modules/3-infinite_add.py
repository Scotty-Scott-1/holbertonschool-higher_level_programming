#!/usr/bin/python3
def infinite_add():
    from sys import argv

    if __name__ == "__main__":
        result = 0
        for i in range(len(argv)):
            if i > 0:
                result += int(argv[i])
    print("{}".format(result))


infinite_add()
