#!/usr/bin/env python3
"""
Task 01 - Pickling Custom Classes
"""

import pickle


class CustomObject:
    """
    CustomObject class with attributes:
    name (str), age (int), is_student (bool)
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display object attributes in a readable format.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the object to a file using pickle.

        Args:
            filename (str): The file path to save the object.

        Returns:
            None
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a pickle file.

        Args:
            filename (str): The file path to read the object from.

        Returns:
            CustomObject or None: Returns the object if successful, else None
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            return obj
        except (OSError, pickle.PickleError):
            return None

