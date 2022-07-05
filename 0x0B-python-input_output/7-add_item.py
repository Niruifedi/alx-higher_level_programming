#!/usr/bin/python3
"""scripts adds all arguments to a python list
    and then save them to a file.
"""

from sys import argv
import json

if __name__ == '__main__':

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    new_list = []
    file_name = "add_item.json"

    for i in argv[1:]:
        new_list.append(i)
    save_to_json_file(new_list, file_name)
    load_from_json_file(file_name)
