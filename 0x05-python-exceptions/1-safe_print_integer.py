#!/usr/bin/python3

"""function that checks and prints integer and handles valueerror exception"""


def safe_print_integer(value):
    while True:
        try:
            if isinstance(value, int) == True:
                print("{:d}".format(value))
                return True
            break
        except ValueError:
            print()
            return False