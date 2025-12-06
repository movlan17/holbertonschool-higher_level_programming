#!/usr/bin/python3
"""
This module contains a function that appends a string to the end
of a UTF-8 text file and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF-8)
    and returns the number of characters added.

    Args:
        filename (str): Name of the file
        text (str): Text to append

    Returns:
        int: Number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

