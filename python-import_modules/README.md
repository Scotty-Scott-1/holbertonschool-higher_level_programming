# Python Import Modules

## Table of Contents
- [Learning Objectives](#learning-objectives)
- [TASK 0](#task-0)
- [TASK 1](#task-1)
- [TASK 2](#task-2)
- [TASK 3](#task-3)
- [TASK 4](#task-4)
- [TASK 5](#task-5)
- [TASK 6](#task-6)
- [TASK 7](#task-7)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone.

Why Python programming is awesome
How to import functions from another file
How to use imported functions
How to create a module
How to use the built-in function dir()
How to prevent code in your script from being executed when imported
How to use command line arguments with your Python programs

### Task 0

#### Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3
```
- You have to use print function with string format to display integers
- You have to assign:
- The value 1 to a variable called a
- The value 2 to a variable called b
- And use those two variables as arguments when calling the functions add and print
- a and b must be defined in 2 different lines: a = 1 and another b = 2
- Your program should print: <a value> + <b value> = <add(a, b) value> followed with a new line
- You can only use the word add_0 once in your code
- You are not allowed to use \* for importing or __import__
- Your code should not be executed when imported - by using __import__, like the example below
```
| GitHub repository: | holbertonschool-higher_level_programming |
| --- | --- |
| Directory: | python-import_modules |
| File: | 0-add.py |

## TASK 1
Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.

Do not use the function print (with string format to display integers) more than 4 times
You have to define:
the value 10 to a variable a
the value 5 to a variable b
and use those two variables only, as arguments when calling functions (including print)
a and b must be defined in 2 different lines: a = 10 and another b = 5
Your program should call each of the imported functions. See example below for format
the word calculator_1 should be used only once in your file
You are not allowed to use \* for importing or \_\_import\_\_
Your code should not be executed when imported

GitHub repository: holbertonschool-higher_level_programming
Directory: python-import_modules
File: 1-calculation.py

## TASK 2
Write a program that prints the number of and the list of its arguments.

The output should be:
Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
: (or . if no arguments were passed) followed by
a new line, followed by (if at least one argument),
one line per argument:
the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
Your code should not be executed when imported
The number of elements of argv can be retrieved by using: len(argv)
You do not have to fully understand lists yet, but imagine that argv can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.

GitHub repository: holbertonschool-higher_level_programming
Directory: python-import_modules
File: 2-args.py


## TASK 3
Write a program that prints the result of the addition of all arguments

The output should be the result of the addition of all arguments, followed by a new line
You can cast arguments into integers by using int() (you can assume that all arguments can be casted into integers)
Your code should not be executed when imported

Last but not least, your program should also handle big numbers. And the good news is: if your program works for the above example, it will work for the following example:

GitHub repository: holbertonschool-higher_level_programming
Directory: python-import_modules
File: 3-infinite_add.py

## TASK 4
Write a program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally in your sandbox using curl).

You should print one name per line, in alpha order
You should print only names that do not start with __
Your code should not be executed when imported
Make sure you are running your code in Python3.8.x (hidden_4.pyc has been compiled with this version)

GitHub repository: holbertonschool-higher_level_programming
Directory: python-import_modules
File: 4-hidden_discovery.py

## TASK 5
Write a program that imports the variable a from the file variable_load_5.py and prints its value.

You are not allowed to use \* for importing or __import__
Your code should not be executed when imported

GitHub repository: holbertonschool-higher_level_programming
Directory: python-import_modules
File: 5-variable_load.py

## TASK 6
Write a program that imports all functions from the file calculator_1.py and handles basic operations.

Usage: ./100-my_calculator.py a operator b
If the number of arguments is not 3, your program has to:
print Usage: ./100-my_calculator.py <a> <operator> <b> followed with a new line
exit with the value 1
operator can be:
+ for addition
- for subtraction
\* for multiplication
/ for division
If the operator is not one of the above:
print Unknown operator. Available operators: +, -, \* and / followed with a new line
exit with the value 1
You can cast a and b into integers by using int() (you can assume that all arguments will be castable into integers)
The result should be printed like this: <a> <operator> <b> = <result>, followed by a new line
You are not allowed to use * for importing or __import__
Your code should not be executed when imported

GitHub repository: holbertonschool-higher_level_programming
Directory: python-import_modules
File: 100-my_calculator.py

## TASK 7
Write a program that prints #pythoniscool, followed by a new line, in the standard output.

Your program should be maximum 2 lines long
You are not allowed to use print or eval or open or import sys in your file 101-easy_print.py

GitHub repository: holbertonschool-higher_level_programming
Directory: python-import_modules
File: 101-easy_print.py
