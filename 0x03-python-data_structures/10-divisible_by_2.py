#!/usr/bin/python3

""" function prints all multiples of 2 in a list"""


def divisible_by_2(my_list=[]):
    booll = my_list[:]
    for count, n in enumerate(my_list):
        if n % 2 == 0:
            booll[count] = True
        else:
            booll[count] = False
    return(booll)
