#!/usr/bin/python3
"""
Module that defines a function that creates a Python object
from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Reads a JSON file and returns the corresponding Python object.

    Args:
        filename (str): The file to read from.

    Returns:
        object: Python object deserialized from JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

