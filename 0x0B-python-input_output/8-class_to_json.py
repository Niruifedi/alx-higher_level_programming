#!/usr/bin/python3
"""class to Json"""


def class_to_json(obj):
    """function returns the dictionary description
        with simple data structure (list, dictionary,string,
        integer and boolean) for Json serialization object
    """
    return obj.__dict__
