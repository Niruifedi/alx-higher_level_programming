#!/usr/bin/python3
"""funtion to read file"""


def read_file(filename=""):
    """function reads out file name
        and prints to stdout.
        Args:
        filename:
        file to read from
    """
    with open(filename, 'r', encoding='UTF-8') as f:
        print(f.read(), end="")
