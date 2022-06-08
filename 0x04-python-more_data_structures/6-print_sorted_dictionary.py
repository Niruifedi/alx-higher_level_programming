#!/usr/bin/python3

""" functioin prints a dictionary by ordered keys """


def print_sorted_dictionary(a_dictionary):
    new_dict = {}

    for i in sorted(a_dictionary):
        print("{}: {}".format(i, a_dictionary[i]))
