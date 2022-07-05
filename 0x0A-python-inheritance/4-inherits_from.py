#!/usr/bin/python3
"""function that returns Boolean value"""


def inherits_from(obj, a_class):
    """returns True if object inherits from a class
        otherwise False.
        Args:
        obj: object to check.
        a_class: class.
    """
    return type(obj) != a_class and isinstance(obj, a_class)
