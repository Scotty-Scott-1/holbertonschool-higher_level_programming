# Python Import Modules

## Table of Contents
- [Learning Objectives](#learning-objectives)
- [Task 0](#task-0) Import a simple function from a simple file
- [Task 1](#task-1) My first toolbox!
- [Task 2](#task-2) How to make a script dynamic!
- [Task 3](#task-3) Infinite addition
- [Task 4](#task-4) Who are you?
- [Task 5](#task-5) Everything can be imported
- [Task 6](#task-6) Build my own calculator
- [Task 7](#task-7) Easy print

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone:
- Why Python programming is awesome
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function dir()
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

### Task 0. Import a simple function from a simple file
#### Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3
- [x] You have to use print function with string format to display integers
- You have to assign:
	- [x] The value 1 to a variable called a
	- [x] The value 2 to a variable called b
	- [x] Use those two variables as arguments when calling the functions add and print
	- [x]  a and b must be defined in 2 different lines: a = 1 and another b = 2
- [x] Your program should print: `<a value>` + `<b value>` = `<add(a, b) value>` followed with a new line
- [x] You can only use the word add_0 once in your code
- [x] You are not allowed to use \* for importing or `__import__`
- [x] Your code should not be executed when imported - by using `__import__`, like the example below

Example:
```
guillaume@ubuntu:~/$ ./0-add.py
1 + 2 = 3
guillaume@ubuntu:~/$ cat 0-import_add.py
__import__("0-add")
guillaume@ubuntu:~/$ python3 0-import_add.py
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-import_modules
File: 0-add.py
Main file: add_0.py
```

### Task 1
#### Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.

- [x] Do not use the function print (with string format to display integers) more than 4 times
- You have to define:
	- [x] The value 10 to a variable a
	- [x] The value 5 to a variable b
	- [x] And use those two variables only, as arguments when calling functions (including print)
	- [x] a and b must be defined in 2 different lines: a = 10 and another b = 5
- [x] Your program should call each of the imported functions. See example below for format
- [x] The word calculator_1 should be used only once in your file
- [x] You are not allowed to use \* for importing or \_\_import\_\_
- [x] Your code should not be executed when imported

Example:
```
guillaume@ubuntu:~/$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-import_modules
File: 1-calculation.py
Main file: calculator_1.py
```

### Task 2
#### Write a program that prints the number of and the list of its arguments.

The output should be:
- [x] Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by: (or . if no arguments were passed) followed by a new line, followed by (if at least one argument),
- [x] One line per argument:
- [x] The position of the argument (starting at 1) followed by :, followed by the argument value and a new line
- [x] Your code should not be executed when imported
- [x] The number of elements of argv can be retrieved by using: len(argv)
- [x] You do not have to fully understand lists yet, but imagine that argv can be used just like a C array: you can use an index to walk through it.
- There are other ways (which will be preferred for future project tasks), if you know them you can use them.

Example:
```
guillaume@ubuntu:~/$ ./2-args.py
0 arguments.
guillaume@ubuntu:~/$ ./2-args.py Hello
1 argument:
1: Hello
guillaume@ubuntu:~/$ ./2-args.py Hello Welcome To The Best School
6 arguments:
1: Hello
2: Welcome
3: To
4: The
5: Best
6: School
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-import_modules
File: 2-args.py
```

### Task 3
#### Write a program that prints the result of the addition of all arguments

- [x] The output should be the result of the addition of all arguments, followed by a new line
- [x] You can cast arguments into integers by using int() (you can assume that all arguments can be casted into integers)
- [x] Your code should not be executed when imported

- [x] Last but not least, your program should also handle big numbers. And the good news is: if your program works for the above example, it will work for the following example:

Example:
```
guillaume@ubuntu:~/$ ./3-infinite_add.py
0
guillaume@ubuntu:~/$ ./3-infinite_add.py 79 10
89
guillaume@ubuntu:~/$ ./3-infinite_add.py 79 10 -40 -300 89
-162
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-import_modules
File: 3-infinite_add.py
```

### Task 4
#### Write a program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally in your sandbox using curl).

- [x] You should print one name per line, in alpha order
- [x] You should print only names that do not start with __
- [x] Your code should not be executed when imported
- [x] Make sure you are running your code in Python3.8.x (hidden_4.pyc has been compiled with this version)

Example:
```
guillaume@ubuntu:~/$ curl -Lso "hidden_4.pyc" "https://github.com/hs-hq/0x02.py/raw/main/hidden_4.pyc"
guillaume@ubuntu:~/$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-import_modules
File: 4-hidden_discovery.py
```

### Task 5
#### Write a program that imports the variable a from the file variable_load_5.py and prints its value.

- [x] You are not allowed to use \* for importing or ```__import__```
- [x] Your code should not be executed when imported

Example:
```
guillaume@ubuntu:~/$ cat variable_load_5.py
#!/usr/bin/python3
a = 98
"""Simple variable
"""

guillaume@ubuntu:~/$ ./5-variable_load.py
98
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-import_modules
File: 5-variable_load.py
Main file: variable_load.py
```

### Task 6
#### Write a program that imports all functions from the file calculator_1.py and handles basic operations.

- [x] Usage: ```./100-my_calculator.py <a> <operator> <b>```
- [x] If the number of arguments is not 3, your program has to:
- [x] print Usage: ./100-my_calculator.py ```<a> <operator> <b>``` followed with a new line
- [x] exit with the value 1
- operator can be:
	- [x] + for addition
	- [x] - for subtraction
	- [x] \* for multiplication
	- [x] / for division
- [x] If the operator is not one of the above: print Unknown operator. Available operators: +, -, \* and / followed with a new line exit with the value 1
- [x] You can cast a and b into integers by using int() (you can assume that all arguments will be castable into integers)
- [x] The result should be printed like this: ```<a> <operator> <b> = <result>```, followed by a new line
- [x] You are not allowed to use * for importing or ```__import__```
Your code should not be executed when imported

Example:
```
guillaume@ubuntu:~/$ ./100-my_calculator.py ; echo $?
Usage: ./100-my_calculator.py <a> <operator> <b>
1
guillaume@ubuntu:~/$ ./100-my_calculator.py 3 + 5 ; echo $?
3 + 5 = 8
0
guillaume@ubuntu:~/$ ./100-my_calculator.py 3 H 5 ; echo $?
Unknown operator. Available operators: +, -, * and /
1
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-import_modules
File: 100-my_calculator.py
Helper module: calculator_1.py
```

### Task 7
#### Write a program that prints #pythoniscool, followed by a new line, in the standard output.

- [x] Your program should be maximum 2 lines long
- [x] You are not allowed to use print or eval or open or import sys in your file 101-easy_print.py

Example:
```
guillaume@ubuntu:~/$ ./101-easy_print.py
#pythoniscool
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-import_modules
File: 101-easy_print.py
Helper module: test.py
```
