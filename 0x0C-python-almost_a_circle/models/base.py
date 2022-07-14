#!/usr/bin/python3
"""Base Class."""
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """load from json string"""
        if json_string is None or len(json_string) == 0:
            return '[]'
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
            Returns an instance with all the attributes already set
        '''
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            pie = Rectangle(3, 8)
        elif cls.__name__ == "Square":
            pie = Square(5)
        pie.update(**dictionary)
        return (pie)

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

    @classmethod
    def load_from_file(cls):
        '''
            loading dict representing the parameters for
            and instance and from that creating instances
        '''
        file_name = cls.__name__ + ".json"

        try:
            with open(file_name, encoding="UTF8") as fd:
                content = cls.from_json_string(fd.read())
        except Exception:
            return []

        instances = []

        for instance in content:
            tmp = cls.create(**instance)
            instances.append(tmp)
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """csv serializzation and deserialization"""
        file_name = cls.__name__ + ".csv"

        with open(file_name, 'w') as f:
            f_csv = csv.writer(f)

            if cls.__name__ == 'Rectangle':
                for item in list_objs:
                    string = ""
                    item = item.to_dictionary()
                    string += (str(item["id"]) + "," +
                               str(item["width"]) + "," +
                               str(item["height"]) + "," +
                               str(item["x"]) + "," + str(item["y"]))
                f_csv.writerow(string)

            if cls.__name__ == 'Square':
                for item in list_objs:
                    string = ""
                    item = item.to_dictionary()
                    string += (str(item["id"]) + "," +
                               str(item["size"]) + "," +
                               str(item["x"]) + "," + str(item["y"]))
                    f_csv.writerow(string)

    @classmethod
    def load_from_file_csv(cls):
        """load csv"""
        return ([])
