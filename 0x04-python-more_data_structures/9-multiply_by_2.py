#!/usr/bin/python3

""" function returns a new dictionary with all values multiplied by 2 """


def multiply_by_2(a_dictionary):
    tmp_dict = a_dictionary.copy()
    for x in tmp_dict.keys():
        tmp_dict[x] *= 2
    return tmp_dict
