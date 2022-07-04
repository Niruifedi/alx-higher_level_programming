#!/usr/bin/python3
"""function to list available attributes and methods"""


def lookup(obj):
    """function looks up an object for attributes and
        method.
        Returns a list.
    """
    attributes = dir(obj)
    return attributes
