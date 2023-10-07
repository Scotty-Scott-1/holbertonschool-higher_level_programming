# Python - Data Structures: Lists, Tuples

## Table of Contents
- [Learning Objectives](#learning-objectives)
- [Task 0](#task-0) Print a list of integers
- [Task 1](#task-1) Secure access to an element in a list
- [Task 2](#task-2) Replace element
- [Task 3](#task-3)
- [Task 4](#task-4)
- [Task 5](#task-5)
- [Task 6](#task-6)
- [Task 7](#task-7)


## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone:

- What are lists and how to use them
- What are the differences and similarities between strings and lists
- What are the most common methods of lists and how to use them
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- What are tuples and how to use them
- When to use tuples versus lists
- What is a sequence
- What is tuple packing
- What is sequence unpacking
- What is the del statement and how to use it



### Task 0
### Print a list of integers
#### Write a function that prints all integers of a list.
- Prototype: def print_list_integer(my_list=[]):
- [x] Format: one integer per line. See example
- [x] You are not allowed to import any module
- [x] You can assume that the list only contains integers
- [x] You are not allowed to cast integers into strings
- [x] You have to use str.format() to print integer

Example:
```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

guillaume@ubuntu:~/$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-data_structures
File: 0-print_list_integer.py
```

### Task 1
### Secure access to an element in a list
#### Write a function that retrieves an element from a list.

- [x] Prototype: def element_at(my_list, idx):
- [x] If idx is negative, the function should return None
- [x] If idx is out of range (> of number of element in my_list), the function should return None
- [x] You are not allowed to import any module
- [x] You are not allowed to use try/except

Example:
```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

guillaume@ubuntu:~/$ ./1-main.py
Element at index 3 is 4
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-data_structures
File: 1-element_at.py
```

### Task 2
### Replace element
#### Write a function that replaces an element of a list at a specific position.

- [x] Prototype: def replace_in_list(my_list, idx, element):
- [x] If idx is negative, the function should not modify anything, and returns the original list
- [x] If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
- [x] You are not allowed to import any module
- [x] You are not allowed to use try/except
- [x] guillaume@ubuntu:~/$ cat 2-main.py

Example:
```
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-data_structures
File: 2-replace_in_list.py
```

### Task 3
### Print a list of integers... in reverse!
#### Write a function that prints all integers of a list, in reverse order.

- [x] Prototype: def print_reversed_list_integer(my_list=[]):
- [x] Format: one integer per line. See example
- [x] You are not allowed to import any module
- [x] You can assume that the list only contains integers
- [x] You are not allowed to cast integers into strings
- [x] You have to use str.format() to print integers

Example:
``
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

guillaume@ubuntu:~/$ ./3-main.py
5
4
3
2
1
guillaume@ubuntu:~/$
``
``
GitHub repository: holbertonschool-higher_level_programming
Directory: python-data_structures
File: 3-print_reversed_list_integer.py
``
