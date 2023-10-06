#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    new_list_1 = []
    product_of_tups = 0
    sum_of_weights = 0

    for tups in my_list:
        num1 = tups[0]
        num2 = tups[1]
        new_list_1.append(num1 * num2)
        sum_of_weights += num2

    for i in new_list_1:
        product_of_tups += i

    return product_of_tups / sum_of_weights
