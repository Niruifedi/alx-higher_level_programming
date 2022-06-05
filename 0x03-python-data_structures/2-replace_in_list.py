#!/usr/bin/python3

"""program replaces an element in a list at specific position"""


def replace_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return(my_list)
