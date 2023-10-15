# Python - Classes and Objects

## Table of Contents
- [Learning Objectives](#learning-objectives)
- [Task 0](#task-0) My first square
- [Task 1](#task-1) Square with size
- [Task 2](#task-2) Size validation
- [Task 3](#task-3) Area of a square
- [Task 4](#task-4) Access and update private attribute
- [Task 5](#task-5) Printing a square
- [Task 6](#task-6) Coordinates of a square



## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone:

- What is OOP
- “first-class everything”
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is self
- What is a method
- What is the special __init__ method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is the __dict__ of a class and/or instance of a class and what does it contain
- How does Python find the attributes of an object or class
- How to use the getattr function

### Task 0
My first square

:dart: Write an empty class `Square` that defines a square:<br>

:white_check_mark: You are not allowed to import any module<br>

Example:
```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

guillaume@ubuntu:~/$ ./0-main.py
<class '0-square.Square'>
{}
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-classes
File: 0-square.py
```

### Task 1
Square with size

:dart: Write a class `Square` that defines a square by: (based on `0-square.py`)<br>

:white_check_mark: Private instance attribute: `size`<br>
:white_check_mark: Instantiation with `size` (no type/value verification)<br>
:white_check_mark: You are not allowed to import any module<br>

Why `size` is private attribute?

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

Example:
```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-classes
File: 1-square.py
```

### Task 2
Size validation

:dart: Write a class `Square` that defines a square by: (based on `1-square.py`)<br>

:white_check_mark: Private instance attribute: `size`<br>

:white_check_mark: Instantiation with optional `size`: `def __init__(self, size=0)`:<br>
- `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`<br>
- if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`<br>

:white_check_mark: You are not allowed to import any module<br>

Example:
```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./2-main.py
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-classes
File: 2-square.py
```

### Task 3
Area of a square

:dart: Write a class `Square` that defines a square by: (based on `2-square.py`)<br>

:white_check_mark: Private instance attribute: `size`

:white_check_mark: Instantiation with optional `size: def __init__(self, size=0):`<br>
- `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`<br>
- if `size` is less than `0`, raise a `ValueErro`r exception with the message `size must be >= 0`<br>

:white_check_mark: Public instance method: `def area(self):` that returns the current square area<br>
:white_check_mark: You are not allowed to import any module<br>

Example:
```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))

guillaume@ubuntu:~/$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-classes
File: 3-square.py
```

### Task 4
Access and update private attribute

:dart: Write a class `Square` that defines a square by: (based on `3-square.py`)<br>

:white_check_mark: Private instance attribute: `size:`<br>
- property `def size(self):` to retrieve it<br>
- property setter `def size(self, value):` to set it:<br>
	- `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`<br>
	- if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`<br>

:white_check_mark: Instantiation with optional `size: def __init__(self, size=0):`<br>
:white_check_mark: Public instance method: `def area(self):` that returns the current square area<br>
:white_check_mark: You are not allowed to import any module<br>

Why a getter and setter?

Reminder: `size` is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.

Example:
```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-classes
File: 4-square.py
```

### Task 5
Printing a square

:dart: Write a class `Square` that defines a square by: (based on `4-square.py`)<br>

:white_check_mark: Private instance attribute: `size:`<br>
- property `def size(self):` to retrieve it<br>
- property setter `def size(self, value):` to set it:<br>
	- `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`<br>
	- if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`<br>

:white_check_mark: Instantiation with optional `size: def __init__(self, size=0):`<br>
:white_check_mark: Public instance method: `def area(self):` that returns the current square area<br>

:white_check_mark: Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:<br>
- if `size` is equal to 0, print an empty line<br>

:white_check_mark: You are not allowed to import any module<br>

Example:
```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

guillaume@ubuntu:~/$ ./5-main.py
###
###
###
--
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
--

--
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-classes
File: 5-square.py
```

### Task 6
Coordinates of a square

:dart: Write a class `Square` that defines a square by: (based on `5-square.py`)

:white_check_mark: Private instance attribute: `size:`<br>
- property `def size(self):` to retrieve it<br>
- property setter `def size(self, value):` to set it:<br>
	- `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`<br>
	- if `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`<br>

- [x] Private instance attribute: `position:`<br>
	- property `def position(self):` to retrieve it<br>
	- property setter `def position(self, value):` to set it:<br>
		- `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`<br>

:white_check_mark: Instantiation with optional `size` and optional `position: def __init__(self, size=0, position=(0, 0))`:
:white_check_mark: Public instance method: `def area(self):` that returns the current square area

- [x] Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
	- if `size` is equal to 0, print an empty line
	- `position` should be use by using space - Don’t fill lines by spaces when `position[1] > 0`

:white_check_mark: You are not allowed to import any module

Example:
```
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

guillaume@ubuntu:~/$ ./6-main.py | tr " " "_" | cat -e
###$
###$
###$
--$
$
_###$
_###$
_###$
--$
___###$
___###$
___###$
--$
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-classes
File: 6-square.py
```
