#!/usr/bin/python3
"""
FileStorage Module
"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Class for serializing instances to a JSON file and deserializing JSON file
    to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file (__file
                    _path) exists)
        """
        try:
            with open(self.__file_path, 'r') as file:
                json_data = file.read()
                obj_dict = json.loads(json_data)

                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    if class_name == 'BaseModel':
                        instance = BaseModel(**value)
                        self.__objects[key] = instance
                    elif class_name == 'User':
                        instance = User(**value)
                    self.__objects[key] = instance

        except FileNotFoundError:
            pass
