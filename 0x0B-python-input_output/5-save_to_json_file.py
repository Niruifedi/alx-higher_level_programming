#!/usr/bin/python3
"""save Json object to file"""
import json


def save_to_json_file(my_obj, filename):
    """function writes an object into a text file
        using json representation
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
