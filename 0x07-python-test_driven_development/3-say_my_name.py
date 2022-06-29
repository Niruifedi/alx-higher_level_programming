#!/usr/bin/python3
"""function prints name"""


def say_my_name(first_name, last_name=""):
    """prints out Name.
    Args:
        first_name: string
        last_name: string

        TypeError:
        first_name must be a string
        last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be strings')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))