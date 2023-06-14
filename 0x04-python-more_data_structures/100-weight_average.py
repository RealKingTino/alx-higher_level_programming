#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:  # Check if the list is empty
        return 0

    sum_product = sum(score * weight for score, weight in my_list)
    sum_weights = sum(weight for score, weight in my_list)
    return sum_product / sum_weights
