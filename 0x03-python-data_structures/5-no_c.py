#!/usr/bin/python3

""" program removes all characters c and C from a string """


def no_c(my_string):
    table = my_string.translate({ord('c'): '', ord('C'): ''})
    return(table)
