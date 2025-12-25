#!/usr/bin/python3
"""
Module that defines a Student class with JSON-serializable dictionary
method, optionally filtered by a list of attributes.
"""


class Student:
    """
    Student class with public attributes first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to include.
                                    If None, all attributes are included.

        Returns:
            dict: Dictionary containing the requested attributes.
        """
        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()

