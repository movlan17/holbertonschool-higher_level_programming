#!/usr/bin/python3
"""
Module that defines a function to convert a class instance
to a dictionary representation suitable for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: Dictionary containing all serializable attributes of obj.
    """
    return obj.__dict__.copy()

