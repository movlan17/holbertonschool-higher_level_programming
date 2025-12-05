#!/usr/bin/python3
"""
Module that defines a function to append text to a file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a UTF-8 text file.

    Args:
        filename (str): File to write to.
        text (str): Text to append.

    Returns:
        int: Number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

