#!/usr/bin/python3
"""
Module that defines a function that returns an object represented
by a JSON string.
"""

import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented
    by a JSON string.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: Python data structure created from the JSON string.
    """
    return json.loads(my_str)

