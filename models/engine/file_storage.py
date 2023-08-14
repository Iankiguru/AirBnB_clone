#!/usr/bin/python3
"""
FileStorage class module.
"""

import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """
    File storage for serializing and deserializing objects to/from JSON files.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary of all objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Set an object in the __objects dictionary.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to the JSON file.
        """
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserialize the JSON file to __objects.
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                objects_data = json.load(file)
                for key, value in objects_data.items():
                    class_name = value["__class__"]
                    if class_name == "BaseModel":
                        instance = BaseModel(**value)
                    elif class_name == "User":
                        instance = User(**value)
                    else:
                        continue
                    FileStorage.__objects[key] = instance
        except FileNotFoundError:
            pass

