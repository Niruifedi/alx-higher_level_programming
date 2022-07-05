#!/usr/bin/python3
"""Json string to object"""
import json


def from_json_string(my_str):
    """function returns an object represented
        by json strings
    """
    return json.loads(my_str)
