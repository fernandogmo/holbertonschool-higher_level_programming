#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and type(my_list) == list:
        scores, weights = 0, 0
        for score, weight in my_list:
            scores += score * weight
            weights += weight
        return scores/weights
    return 0
