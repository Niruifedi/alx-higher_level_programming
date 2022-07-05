#!/usr/bin/python3
"""function appends string at the end of a text file with UTF8 encoding"""


def append_write(filename="", text=""):
    """function appends a string to the end of file
        and returns the number of characters added
    """
    with open(filename, 'a', encoding="UTF-8") as f:
        return f.write(text)
