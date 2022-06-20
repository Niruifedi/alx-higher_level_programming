#!/usr/bin/python3

"""function that checks and prints integer and handles valueerror exception"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
