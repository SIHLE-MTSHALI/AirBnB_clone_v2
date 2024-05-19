#!/usr/bin/python3
"""FileStorage class module"""

import json


class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for key, obj in obj_dict.items():
                cls_name = key.split('.')[0]
                cls = eval(cls_name)
                FileStorage.__objects[key] = cls(**obj)
        except FileNotFoundError:
            pass

    def close(self):
        """Call reload() method for deserializing the JSON file to objects"""
        self.reload()
