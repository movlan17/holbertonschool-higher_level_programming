#!/usr/bin/python3
"""
Module 2-append_write

This module provides a function that appends a string to the end of a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF-8 text file and returns the number
    of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to write into the file.

    Returns:
        int: The number of characters added to the file.

    Notes:
        - If the file does not exist, it will be created.
        - You must use the with statement.
        - No imports are allowed.
        - Do not handle permission errors or missing file errors explicitly.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

