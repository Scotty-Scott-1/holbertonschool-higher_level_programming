def print_sorted_dictionary(a_dictionary):

    sorted_dict = {}
    sorted_dict = sorted(a_dictionary.items())

    for keys, value in sorted_dict:
        print(keys, value)
