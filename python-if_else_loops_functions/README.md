# Python - if/else, loops, functions

## Table of Contents
- [Learning Objectives](#learning-objectives)
- [Task 0](#task-0) Print whether the number stored in the variable number is positive or negative
- [Task 1](#task-1) Print the last digit of the number stored in the variable number
- [Task 2](#task-2) Print the ASCII alphabet, in lowercase, not followed by a new line
- [Task 3](#task-3) Infinite addition
- [Task 4](#task-4) Who are you?
- [Task 5](#task-5) Everything can be imported
- [Task 6](#task-6) Build my own calculator
- [Task 7](#task-7) Easy print



## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone:
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

### Task 0. Positive anything is better than negative nothing
#### This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.
- [x] The variable number will store a different value every time you will run this program
- [x] You don’t have to understand what import, random. randint do. Please do not touch this code
- The output of the program should be:
	- [x] `The number`, followed by
		- [x] if the number is greater than 0: `is positive`
		- [x] if the number is 0: `is zero`
		- [x] if the number is less than 0: `is negative`
		- [x] followed by a new line

Example:
```
guillaume@ubuntu:~/$ ./0-positive_or_negative.py
-4 is negative
guillaume@ubuntu:~/$ ./0-positive_or_negative.py
0 is zero
guillaume@ubuntu:~/$ ./0-positive_or_negative.py
-3 is negative
guillaume@ubuntu:~/$ ./0-positive_or_negative.py
-10 is negative
guillaume@ubuntu:~/$ ./0-positive_or_negative.py
10 is positive
guillaume@ubuntu:~/$ ./0-positive_or_negative.py
-5 is negative
guillaume@ubuntu:~/$ ./0-positive_or_negative.py
6 is positive
guillaume@ubuntu:~/$ ./0-positive_or_negative.py
7 is positive
guillaume@ubuntu:~/$ ./0-positive_or_negative.py
5 is positive
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-if_else_loops_functions
File: 0-positive_or_negative.py
```

### Task 1. The last digit
#### This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.
- [x] The variable number will store a different value every time you will run this program
- [x] This line should not change: number = random.randint(-10000, 10000)
- The output of the program should be:
	- [x] The string `Last digit of`
	- [x] followed by the `<numbe>r`
	- [x] followed by the string `is`
	- [x] followed by the `<last digit of number>`
- followed by
	- [x] if the last digit is greater than 5: the string `and is greater than 5`
	- [x] if the last digit is 0: the string `and is 0`
	- [x] if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
	- [x] followed by a new line

Example:
```
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of 1144 is 4 and is less than 6 and not 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of -9200 is 0 and is 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of 5247 is 7 and is greater than 5
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of 3369 is 9 and is greater than 5
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of -5224 is -4 and is less than 6 and not 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of -4485 is -5 and is less than 6 and not 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of 3850 is 0 and is 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of 5169 is 9 and is greater than 5
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-if_else_loops_functions
File: 1-last_digit.py
```

### Task 2
#### Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
- [x] Use only one print function with string format
- [x] Use only one loop in your code
- [x] You are not allowed to store characters in a variable
- [x] You are not allowed to import any module

Example:
```
guillaume@ubuntu:~/$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyzguillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-if_else_loops_functions
File: 2-print_alphabet.py
```
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
