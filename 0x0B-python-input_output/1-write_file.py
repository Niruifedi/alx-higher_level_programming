#!/usr/bin/python3
"""funtion that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """this function writes into a file
        Args:
        filename:
        file to write into
        text:
        text to write into the file
    """
    with open(filename, 'w', encoding="UTF-8") as f:
        return f.write(text)
