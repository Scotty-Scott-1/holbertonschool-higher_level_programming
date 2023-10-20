#!/usr/bin/python3
"""save command line to args to list. save to a json file. load file"""


from sys import argv


save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file

my_list = []
for arg in argv:
    my_list.append(arg)
my_list.pop(0)

save_to(my_list, "add_item.json")
print(load_from("add_item.json"))
