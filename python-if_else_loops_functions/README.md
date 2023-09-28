Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why indentation is so important in Python
How to use the if, if ... else statements
How to use comments
How to affect values to variables
How to use the while and for loops
How to use the break and continues statements
How to use else clauses on loops
What does the pass statement do, and when to use it
How to use range
What is a function and how do you use functions
What does return a function that does not use any return statement
Scope of variables
What’s a traceback
What are the arithmetic operators and how to use them

Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.*)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.7.*)
All your files must be executable
The length of your files will be tested using wc


TASK 0
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.

You can find the source code here
The variable number will store a different value every time you will run this program
You don’t have to understand what import, random. randint do. Please do not touch this code
The output of the program should be:
The number, followed by
if the number is greater than 0: is positive
if the number is 0: is zero
if the number is less than 0: is negative
followed by a new line

GitHub repository: holbertonschool-higher_level_programming
Directory: python-if_else_loops_functions
File: 0-positive_or_negative.py


TASK 1
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.

You can find the source code here
The variable number will store a different value every time you will run this program
You don’t have to understand what import, random.randint do. Please do not touch this code. This line should not change: number = random.randint(-10000, 10000)
The output of the program should be:
The string Last digit of, followed by
the number, followed by
the string is, followed by the last digit of number, followed by
if the last digit is greater than 5: the string and is greater than 5
if the last digit is 0: the string and is 0
if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
followed by a new line

GitHub repository: holbertonschool-higher_level_programming
Directory: python-if_else_loops_functions
File: 1-last_digit.py

TASK 2
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

Use only one print function with string format
Use only one loop in your code
You are not allowed to store characters in a variable
You are not allowed to import any module

GitHub repository: holbertonschool-higher_level_programming
Directory: python-if_else_loops_functions
File: 2-print_alphabet.py

Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

TASK 3
Print all the letters except q and e
You can only use one print function with string format
You can only use one loop in your code
You are not allowed to store characters in a variable
You are not allowed to import any module

GitHub repository: holbertonschool-higher_level_programming
Directory: python-if_else_loops_functions
File: 3-print_alphabt.py

TASK 4
Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example)

You can only use one print function with string format
You can only use one loop in your code
You are not allowed to store numbers or strings in a variable
You are not allowed to import any module

GitHub repository: holbertonschool-higher_level_programming
Directory: python-if_else_loops_functions
File: 4-print_hexa.py

TASK 5
Write a program that prints numbers from 0 to 99.

Numbers must be separated by ,, followed by a space
Numbers should be printed in ascending order, with two digits
The last number should be followed by a new line
You can only use no more than 2 print functions with string format
You can only use one loop in your code
You are not allowed to store numbers or strings in a variable
You are not allowed to import any module

GitHub repository: holbertonschool-higher_level_programming
Directory: python-if_else_loops_functions
File: 5-print_comb2.py

TASK 6
Write a program that prints all possible different combinations of two digits.

Numbers must be separated by ,, followed by a space
The two digits must be different
01 and 10 are considered the same combination of the two digits 0 and 1
Print only the smallest combination of two digits
Numbers should be printed in ascending order, with two digits
The last number should be followed by a new line
You can only use no more than 3 print functions with string format
You can only use no more than 2 loops in your code
You are not allowed to store numbers or strings in a variable
You are not allowed to import any module

GitHub repository: holbertonschool-higher_level_programming
Directory: python-if_else_loops_functions
File: 6-print_comb3.py


TASK 7
Write a function that checks for lowercase character.

Prototype: def islower(c):
Returns True if c is lowercase
Returns False otherwise
You are not allowed to import any module
You are not allowed to use str.upper() and str.isupper()
Tips: ord()
You don’t need to understand __import__

GitHub repository: holbertonschool-higher_level_programming
Directory: python-if_else_loops_functions
File: 7-islower.py

TASK 8
Write a function that prints a string in uppercase followed by a new line.

Prototype: def uppercase(str):
You can only use no more than 2 print functions with string format
You can only use one loop in your code
You are not allowed to import any module
You are not allowed to use str.upper() and str.isupper()
Tips: ord()

GitHub repository: holbertonschool-higher_level_programming
Directory: python-if_else_loops_functions
File: 8-uppercase.py

TASK 9
Write a function that prints the last digit of a number.

Prototype: def print_last_digit(number):
Returns the value of the last digit
You are not allowed to import any module
You don’t need to understand __import__

GitHub repository: holbertonschool-higher_level_programming
Directory: python-if_else_loops_functions
File: 9-print_last_digit.py

TASK 10
Write a function that adds two integers and returns the result.

Prototype: def add(a, b):
Returns the value of a + b
You are not allowed to import any module

GitHub repository: holbertonschool-higher_level_programming
Directory: python-if_else_loops_functions
File: 10-add.py

TASK 11
Write a function that computes a to the power of b and return the value.

Prototype: def pow(a, b):
Returns the value of a ^ b
You are not allowed to import any module

GitHub repository: holbertonschool-higher_level_programming
Directory: python-if_else_loops_functions
File: 11-pow.py

TASK 12
Write a function that prints the numbers from 1 to 100 separated by a space.

For multiples of three print Fizz instead of the number and for multiples of five print Buzz.
For numbers which are multiples of both three and five print FizzBuzz.
Prototype: def fizzbuzz():
Each element should be followed by a space
You are not allowed to import any module

GitHub repository: holbertonschool-higher_level_programming
Directory: python-if_else_loops_functions
File: 12-fizzbuzz.py

TASK 13
Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line.

You can only use one print function with string format
You can only use one loop in your code
You are not allowed to store characters in a variable
You are not allowed to import any module

GitHub repository: holbertonschool-higher_level_programming
Directory: python-if_else_loops_functions
File: 100-print_tebahpla.py


TASK 14
Write a function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”).

Prototype: def remove_char_at(str, n):
You are not allowed to import any module
You don’t need to understand __import__

GitHub repository: holbertonschool-higher_level_programming
Directory: python-if_else_loops_functions
File: 101-remove_char_at.py
