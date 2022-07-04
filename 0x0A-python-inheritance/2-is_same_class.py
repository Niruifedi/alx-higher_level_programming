#!/usr/bin/python3
"""function that returns Boolean value"""


def is_same_class(obj, a_class):
    """returns True if object is an instance
        otherwise False.
        Args:
        obj: object to check.
        a_class: class.
    """
    if type(obj) == a_class:
        return True
    return False
