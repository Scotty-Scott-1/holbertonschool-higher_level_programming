#!/usr/bin/python3

for i in range(0, 10):
    for j in range(0, 10):
        if (i < j):
            if (str(i) + str(j) != "89"):
                print("{}{}".format(i, j), end=", ")
print("89")
