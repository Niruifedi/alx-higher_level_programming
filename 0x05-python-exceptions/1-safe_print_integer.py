#!/usr/bin/python3

"""function that checks and prints integer and handles valueerror exception"""


def safe_print_integer(value):
    while True:
        try:
            if isinstance(value, int):
                print("{:d}".format(value))
                return True
        except ValueError:
            print()
            return False
