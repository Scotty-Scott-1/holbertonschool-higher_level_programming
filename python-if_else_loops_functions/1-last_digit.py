#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)

if number < 0:
    last_digit = "-" + number_str[-1]
else:
    last_digit = number_str[-1]

print("Last digit of {} is {}".format(number, last_digit), end=" ")
if int(last_digit) > 5:
    print("and is greater than 5")
elif int(last_digit) == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
