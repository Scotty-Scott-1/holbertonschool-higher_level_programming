# Python - More Data Structures: Set, Dictionary

## Table of Contents
- [Learning Objectives](#learning-objectives)
- [Task 0](#task-0) Squared simple
- [Task 1](#task-1) Search and replace
- [Task 2](#task-2) Unique addition
- [Task 3](#task-3) Present in both
- [Task 4](#task-4) Only differents
- [Task 5](#task-5) Number of keys
- [Task 6](#task-6) Print sorted dictionary
- [Task 7](#task-7) Update dictionary
- [Task 8](#task-8) Simple delete by key
- [Task 9](#task-9) Multiply by 2
- [Task 10](#task-10) Best score
- [Task 11](#task-11) Multiply by using map
- [Task 12](#task-12) Roman to Integer
- [Task 13](#task-11) Weighted average!
- [Task 14](#task-12) Squared by using map


## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone:

- Why Python programming is awesome
- What are sets and how to use them
- What are the most common methods of set and how to use them
- When to use sets versus lists
- How to iterate into a set
- What are dictionaries and how to use them
- When to use dictionaries versus lists or sets
- What is a key in a dictionary
- How to iterate over a dictionary
- What is a lambda function
- What are the map, reduce and filter functions


### Task 0
Squared simple

:dart: Write a function that computes the square value of all integers of a matrix.<br>
:white_check_mark: Prototype: `def square_matrix_simple(matrix=[]):`<br>
:white_check_mark: `matrix` is a 2 dimensional array<br>
:ballot_box_with_check: Returns a new matrix:<br>
:ballot_box_with_check: Same size as `matrix`.<br>
:ballot_box_with_check: Each value should be the square of the value of the input :arrow_heading_up:<br>
:white_check_mark: Initial matrix should not be modified<br>
:white_check_mark: You are not allowed to import any module<br>
:white_check_mark: You are allowed to use regular loops, `map`, etc.<br>

Example:
```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

guillaume@ubuntu:~/$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-more_data_structures
File: 0-square_matrix_simple.py
```

### Task 1
Search and replace

:dart:Write a function that replaces all occurrences of an element by another in a new list.<br>
:white_check_mark: Prototype: `def search_replace(my_list, search, replace):`<br>
:white_check_mark: `my_list` is the initial list<br>
:white_check_mark: `search` is the element to replace in the list<br>
:white_check_mark: `replace` is the new element<br>
:white_check_mark: You are not allowed to import any module<br>

Example:
```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)

guillaume@ubuntu:~/$ ./1-main.py
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-more_data_structures
File: 1-search_replace.py
```

### Task 2.
Unique addition

:dart: Write a function that adds all unique integers in a list (only once for each integer).<br>
:white_check_mark: `Prototype: def uniq_add(my_list=[]):`<br>
:white_check_mark: You are not allowed to import any module<br>

Example:
```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))

guillaume@ubuntu:~/$ ./2-main.py
Result: 15
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-more_data_structures
File: 2-uniq_add.py
```

### Task 3
Present in both

:dart: Write a function that returns a set of common elements in two sets.<br>
:white_check_mark: Prototype: `def common_elements(set_1, set_2):`<br>
:white_check_mark: You are not allowed to import any module<br>

Example:
```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

guillaume@ubuntu:~/$ ./3-main.py
['C']
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-more_data_structures
File: 3-common_elements.py
```

### Task 4
Only differents

:dart: Write a function that returns a set of all elements present in only one set.<br>
:white_check_mark: Prototype: def only_diff_elements(set_1, set_2):<br>
:white_check_mark: You are not allowed to import any module<br>

Eaxmple:
```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))

guillaume@ubuntu:~/$ ./4-main.py
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-more_data_structures
File: 4-only_diff_elements.py
```

### Task 5
Number of keys

:dart: Write a function that returns the number of keys in a dictionary.<br>
:white_check_mark: Prototype: `def number_keys(a_dictionary):`<br>
:white_check_mark: You are not allowed to import any module<br>

Example:
```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
number_keys = __import__('5-number_keys').number_keys

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))

guillaume@ubuntu:~/$ ./5-main.py
Number of keys: 3
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-more_data_structures
File: 5-number_keys.py
```

### Task 6
Print sorted dictionary

:dart: Write a function that prints a dictionary by ordered keys.<br>
:white_check_mark: `Prototype: def print_sorted_dictionary(a_dictionary):`<br>
:white_check_mark: You can assume that all keys are strings<br>
:white_check_mark: Keys should be sorted by alphabetic order<br>
:white_check_mark: Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)<br>
:white_check_mark: Dictionary values can have any type<br>
:white_check_mark: You are not allowed to import any module<br>

Example:
```
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)

guillaume@ubuntu:~/$ ./6-main.py
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-more_data_structures
File: 6-print_sorted_dictionary.py
```

### Task 7
Update dictionary

:dart: Write a function that replaces or adds key/value in a dictionary.<br>
:white_check_mark: Prototype: `def update_dictionary(a_dictionary, key, value):`<br>
:white_check_mark: `key` argument will be always a string<br>
:white_check_mark: `value` argument will be any type<br>
:white_check_mark: If a key exists in the dictionary, the value will be replaced<br>
:white_check_mark: If a key doesn’t exist in the dictionary, it will be created<br>
:white_check_mark: You are not allowed to import any module<br>
```
guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

guillaume@ubuntu:~/$ ./7-main.py
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-more_data_structures
File: 7-update_dictionary.py
```
### Task 8
Simple delete by key

:dart: Write a function that deletes a key in a dictionary.<br>
:white_check_mark: Prototype: `def simple_delete(a_dictionary, key="")`<br>
:white_check_mark: `key` argument will be always a string<br>
:white_check_mark: If a key doesn’t exist, the dictionary won’t change<br>
:white_check_mark: You are not allowed to import any module<br>
```
Example:
guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
simple_delete = __import__('8-simple_delete').simple_delete
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = simple_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

guillaume@ubuntu:~/$ ./8-main.py
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
--
--
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-more_data_structures
File: 8-simple_delete.py
```

### Task 9
Multiply by 2

:dart: Write a function that returns a new dictionary with all values multiplied by 2<br>
:white_check_mark: Prototype: `def multiply_by_2(a_dictionary):`<br>
:white_check_mark: You can assume that all values are only integers<br>
:white_check_mark: Returns a new dictionary<br>
:white_check_mark: You are not allowed to import any module<br>

Example:
```
guillaume@ubuntu:~/$ cat 9-main.py

#!/usr/bin/python3
multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

guillaume@ubuntu:~/$ ./9-main.py
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-more_data_structures
File: 9-multiply_by_2.py
```

### Task 10
Best score

:dart: Write a function that returns a key with the biggest integer value.<br>
:white_check_mark: Prototype: `def best_score(a_dictionary):`<br>
:white_check_mark: You can assume that all values are only integers<br>
:white_check_mark: If no score found, return `None`<br>
:white_check_mark: You can assume all students have a different score<br>
:white_check_mark: You are not allowed to import any module<br>

Example:
```
guillaume@ubuntu:~/$ cat 10-main.py
#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))

guillaume@ubuntu:~/$ ./10-main.py
Best score: Molly
Best score: None
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-more_data_structures
File: 10-best_score.py
```

### Task 11
Multiply by using map

:dart: Write a function that returns a list with all values multiplied by a number without using any loops.<br>
:white_check_mark: Prototype: `def multiply_list_map(my_list=[], number=0):`<br>
:ballot_box_with_check: Returns a new list:<br>
:ballot_box_with_check: Same length as my_list<br>
:ballot_box_with_check: Each value should be multiplied by number :arrow_heading_up:<br>
:white_check_mark: Initial list should not be modified<br>
:white_check_mark: You are not allowed to import any module<br>
:white_check_mark: You have to use map<br>
:white_check_mark: Your file should be max 3 lines<br>

Example:
```
guillaume@ubuntu:~/$ cat 11-main.py
#!/usr/bin/python3
multiply_list_map = __import__('11-multiply_list_map').multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)

guillaume@ubuntu:~/$ ./11-main.py
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-more_data_structures
File: 11-multiply_list_map.py
```

### Task 12
Roman to Integer
```
Technical interview preparation:
You are not allowed to google anything
Whiteboard first
```
:dart: Create a function `def roman_to_int(roman_string):` that converts a Roman numeral to an integer.<br>
:white_check_mark: You can assume the number will be between 1 to 3999.<br>
:white_check_mark:`def roman_to_int(roman_string)` must return an integer<br>
:white_check_mark: If the `roman_string` is not a string or `None`, return `0`<br>

Example:
```
guillaume@ubuntu:~/$ cat 12-main.py
#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

guillaume@ubuntu:~/$ ./12-main.py
X = 10
VII = 7
IX = 9
LXXXVII = 87
DCCVII = 707
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-more_data_structures
File: 12-roman_to_int.py
```

### Task 13
Weighted average!

:dart: Write a function that returns the weighted average of all integers tuple `(<score>, <weight>)`<br>
:white_check_mark: Prototype: `def weight_average(my_list=[]):`<br>
:white_check_mark: Returns `0` if the list is empty<br>
:white_check_mark: You are not allowed to import any module<br>

Example:
```
guillaume@ubuntu:~/$ cat 100-main.py
#!/usr/bin/python3
weight_average = __import__('100-weight_average').weight_average

my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))

guillaume@ubuntu:~/$ ./100-main.py
Average: 2.80
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-more_data_structures
File: 100-weight_average.py
```

### Task 14
Squared by using map

:dart: Write a function that computes the square value of all integers of a matrix using `map`<br>
:white_check_mark: Prototype: `def square_matrix_map(matrix=[]):`<br>
:white_check_mark: `matrix` is a 2 dimensional array<br>
:ballot_box_with_check: Returns a new matrix:<br>
:ballot_box_with_check: Same size as `matrix`<br>
:ballot_box_with_check: Each value should be the square of the value of the input<br>
:white_check_mark: Initial matrix should not be modified<br>
:white_check_mark: You are not allowed to import any module<br>
:white_check_mark: You have to use `map`<br>
:white_check_mark: You are not allowed to use `for` or `while`<br>
:white_check_mark: Your file should be max 3 lines<br>

Example:
```
guillaume@ubuntu:~/$ cat 101-main.py
#!/usr/bin/python3
square_matrix_map = \
    __import__('101-square_matrix_map').square_matrix_map

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_map(matrix)
print(new_matrix)
print(matrix)

guillaume@ubuntu:~/$ ./101-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
guillaume@ubuntu:~/$
```
```
GitHub repository: holbertonschool-higher_level_programming
Directory: python-more_data_structures
File: 101-square_matrix_map.py
```
