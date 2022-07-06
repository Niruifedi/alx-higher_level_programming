#!/usr/bin/python3
"""Student to Json"""


class Student:
    """class defines student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dictionaryu representation"""
        return self.__dict__
