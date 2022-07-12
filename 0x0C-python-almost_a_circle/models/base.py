#!/usr/bin/python3
"""Base Class."""
import json


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiation constructor
            id: can only accept integer value
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ converting a dict into a json string"""
        if list_dictionaries is None:
            return "[]"
        else:
            json_str = json.dumps(list_dictionaries)
        return json_str

    @classmethod
    def save_to_file(cls, list_objs):
        '''
            Writes the string representation of an object of a class
            into a file
        '''
        file_name = cls.__name__ + ".json"
        content = []
        if list_objs is not None:
            for item in list_objs:
                item = item.to_dictionary()
                json_dict = json.loads(cls.to_json_string(item))
                content.append(json_dict)
        with open(file_name, "w") as f:
            json.dump(content, f)
