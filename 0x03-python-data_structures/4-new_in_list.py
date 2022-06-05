#!/usr/bin/python3

"""program to replace an element in a list and returns the original list"""


def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if 0 <= idx < len(my_list):
        new_list[idx] = element
        return(new_list)
    return(my_list)
