#!/usr/bin/env python3
"""
Basic Serialization Module
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The output filename. If file exists, it will be replaced.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads a JSON file and deserializes it into a Python dictionary.

    Args:
        filename (str): The JSON filename to read.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

