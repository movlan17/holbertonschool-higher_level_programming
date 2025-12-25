#!/usr/bin/python3
"""
Module that defines a function that returns the JSON representation
of an object.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized into JSON format.

    Returns:
        str: JSON string representation of the object.
    """
    return json.dumps(my_obj)

