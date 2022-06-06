#!/usr/bin/python3

""" function that finds the biggest integer in a list"""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return ("None")
    big_n = my_list[0]
    for n in my_list:
        if n > big_n:
            big_n = n
    return (big_n)
