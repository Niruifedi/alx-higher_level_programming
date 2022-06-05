#!/usr/bin/python3

"""prints an integer list in reversed order"""


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for i in reversed(my_list):
        print("{:d}".format(i))
