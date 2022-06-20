#!/usr/bin/python3

"""function prints elements of a list and handles the exceptions"""


def safe_print_list(my_list=[], x=0):
    index = 0
    while True:
        try:
            if index < x:
                print(my_list[index], end='')
                index += 1
            else:
                print()
                return index
        except IndexError:
            print()
            return index
