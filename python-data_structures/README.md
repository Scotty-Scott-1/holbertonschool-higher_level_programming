# Python - Data Structures: Lists, Tuples

## Table of Contents
- [Learning Objectives](#learning-objectives)
- [Task 0](#task-0) Print a list of integers
- [Task 1](#task-1) Secure access to an element in a list
- [Task 2](#task-2) Replace element
- [Task 3](#task-3) Print a list of integers... in reverse!
- [Task 4](#task-4) Replace in a copy
- [Task 5](#task-5) Can you C me now?
- [Task 6](#task-6) Lists of lists = Matrix
- [Task 7](#task-7) Tuples addition
- [Task 8](#task-8) More returns!
- [Task 9](#task-9) Find the max
- [Task 10](#task-10) Only by 2
- [Task 11](#task-11) Delete at
- [Task 12](#task-12) Tuples addition

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
Print a list of integers

:dart: Write a function that prints all integers of a list.<br>
:white_check_mark: Prototype: `def print_list_integer(my_list=[]):`<br>
:white_check_mark: Format: one integer per line. See example<br>
:white_check_mark: You are not allowed to import any module<br>
:white_check_mark: You can assume that the list only contains integers<br>
:white_check_mark: You are not allowed to cast integers into strings<br>
:white_check_mark: You have to use `str.format()` to print integer<br>

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
Secure access to an element in a list

:dart: Write a function that retrieves an element from a list.<br>
:white_check_mark: Prototype: `def element_at(my_list, idx):`<br>
:white_check_mark: If `idx` is negative, the function should return `None`<br>
:white_check_mark: If `idx` is out of range (> of number of element in my_list), the function should return `None`<br>
:white_check_mark: You are not allowed to import any module<br>
:white_check_mark: You are not allowed to use `try/except`<br>

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
Replace element

:dart: Write a function that replaces an element of a list at a specific position.<br>
:white_check_mark: Prototype: `def replace_in_list(my_list, idx, element):`<br>
:white_check_mark:  If `idx` is negative, the function should not modify anything, and returns the original list<br>
:white_check_mark:  If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list<br>
:white_check_mark:  You are not allowed to import any module<br>
:white_check_mark:  You are not allowed to use `try/except`<br>

Example:
```
guillaume@ubuntu:~/$ cat 2-main.py
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
Print a list of integers... in reverse!

:dart: Write a function that prints all integers of a list, in reverse order.<br>
:white_check_mark:  Prototype: `def print_reversed_list_integer(my_list=[]):`<br>
:white_check_mark:  Format: one integer per line. See example<br>
:white_check_mark:  You are not allowed to import any module<br>
:white_check_mark:  You can assume that the list only contains integers<br>
:white_check_mark:  You are not allowed to cast integers into strings<br>
:white_check_mark:  You have to use `str.format()` to print integers<br>

Example:
```
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
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-data_structures
File: 3-print_reversed_list_integer.py
```

### Task 4
Replace in a copy

:dart: Write a function that replaces an element in a list at a specific position without modifying the original list.<br>
:white_check_mark: Prototype: `def new_in_list(my_list, idx, element):`<br>
:white_check_mark: If `idx` is negative, the function should return a copy of the original list<br>
:white_check_mark: If `idx` is out of range (> of number of element in `my_list`), the function should return a copy of the original list<br>
:white_check_mark: You are not allowed to import any module<br>
:white_check_mark: You are not allowed to use `try/except`<br>

Example:
```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-data_structures
File: 4-new_in_list.py
```

### Task 5
Can you C me now?<br>

:dart: Write a function that removes all characters c and C from a string.<br>
:white_check_mark: Prototype: `def no_c(my_string):`<br>
:white_check_mark: The function should return the new string<br>
:white_check_mark: You are not allowed to import any module<br>
:white_check_mark: You are not allowed to use `str.replace()`<br>

Example:
```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
no_c = __import__('5-no_c').no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

guillaume@ubuntu:~/$ ./5-main.py
Best Shool
hiago
 is fun!
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-data_structures
File: 5-no_c.py
```

### Task 6
Lists of lists = Matrix

:dart: Write a function that prints a matrix of integers.<br>
:white_check_mark: Prototype: `def print_matrix_integer(matrix=[[]]):`<br>
:white_check_mark: You are not allowed to import any module<br>
:white_check_mark: You can assume that the list only contains integers<br>
:white_check_mark: You are not allowed to cast integers into strings<br>
:white_check_mark: You have to use `str.format()` to print integers<br>

Example:
```
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

guillaume@ubuntu:~/$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-data_structures
File: 6-print_matrix_integer.py
```



### Task 7
Tuples addition

:dart: Write a function that adds 2 tuples.<br>
:white_check_mark: Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`<br>
:white_check_mark: Returns a tuple with 2 integers:<br>
:white_check_mark: The first element should be the addition of the first element of each argument<br>
:white_check_mark: The second element should be the addition of the second element of each argument<br>
:white_check_mark: You are not allowed to import any module<br>
:white_check_mark: You can assume that the two tuples will only contain integers<br>
:white_check_mark: If `a tuple` is smaller than 2, use the value `0` for each missing integer<br>
:white_check_mark: If `a tuple` is bigger than 2, use only the first 2 integers<br>

Example:
```
guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

guillaume@ubuntu:~/$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
guillaume@ubuntu:~/$
```
```

GitHub repository: holbertonschool-higher_level_programming
Directory: python-data_structures
File: 7-add_tuple.py
```

### Task 8
More returns!

:dart: Write a function that returns a tuple with the length of a string and its first character.<br>
:white_check_mark: Prototype: `def multiple_returns(sentence):`<br>
:white_check_mark: If the sentence is empty, the first character should be equal to `None`<br>
:white_check_mark: You are not allowed to import any module<br>

Example:
```
guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

guillaume@ubuntu:~/$ ./8-main.py
Length: 22 - First character: A
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-data_structures
File: 8-multiple_returns.py`
```


### Task 9
Find the max

:dart: Write a function that finds the biggest integer of a list.<br>
:white_check_mark: Prototype: `def max_integer(my_list=[]):`<br>
:white_check_mark: If the list is empty, return `None`<br>
:white_check_mark: You can assume that the list only contains integers<br>
:white_check_mark: You are not allowed to import any module<br>
:white_check_mark: You are not allowed to use the builtin `max()`<br>

Example:
```
guillaume@ubuntu:~/$ cat 9-main.py
#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

guillaume@ubuntu:~/$ ./9-main.py
Max: 90
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-data_structures
File: 9-max_integer.py
```

### Task 10
Only by 2
:dart: Write a function that finds all multiples of 2 in a list.

:white_check_mark: Prototype: `def divisible_by_2(my_list=[]):`<br>
:white_check_mark: Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2<br>
:white_check_mark: The new list should have the same size as the original list<br>
:white_check_mark: You are not allowed to import any module<br>

Example:
```
guillaume@ubuntu:~/$ cat 10-main.py
#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

guillaume@ubuntu:~/$ ./10-main.py
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-data_structures
File: 10-divisible_by_2.py
```

### Task 11
Delete at

:dart: Write a function that deletes the item at a specific position in a list.<br>
:white_check_mark: Prototype: `def delete_at(my_list=[], idx=0):`<br>
:white_check_mark: If `idx` is negative or out of range, nothing change (returns the same list)<br>
:white_check_mark: You are not allowed to use `pop()`<br>
:white_check_mark: You are not allowed to import any module<br>

Example:
```
guillaume@ubuntu:~/$ cat 11-main.py
#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

guillaume@ubuntu:~/$ ./11-main.py
[1, 2, 3, 5]
[1, 2, 3, 5]
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-data_structures
File: 11-delete_at.py
```

### Task 12
Switch

:dart: Complete the source code in order to switch value of `a` and `b`<br>
:dart: You can find the source code below<br>
:white_check_mark: Your code should be inserted where the comment is (line 4)<br>
:white_check_mark: Your program should be exactly 5 lines long<br>

Source code:
```
#!/usr/bin/python3
a = 89
b = 10
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print("a={:d} - b={:d}".format(a, b))
```
Example:
```
guillaume@ubuntu:~/py/$ ./12-switch.py
a=10 - b=89
guillaume@ubuntu:~/py/$ wc -l 12-switch.py
5 12-switch.py
guillaume@ubuntu:~/py/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-data_structures
File: 12-switch.py
```
