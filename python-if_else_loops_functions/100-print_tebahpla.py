#!/usr/bin/python3
j = 123

for i in range(97, 123):
    j-=1
    if j % 2 == 1:
        print("{}".format(chr(j - 32)), end="")
    elif j % 2 == 0:
        print("{}".format(chr(j)), end="")
print()
