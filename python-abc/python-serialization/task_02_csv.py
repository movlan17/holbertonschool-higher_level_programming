#!/usr/bin/env python3
"""
Task 02 - Convert CSV data to JSON format
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV file to JSON file named 'data.json'.

    Args:
        csv_filename (str): Path to the CSV file.

    Returns:
        bool: True if successful, False if any error occurs.
    """
    try:
        data_list = []

        with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_list.append(row)

        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(data_list, jsonfile, indent=4)

        return True

    except (FileNotFoundError, OSError, csv.Error, json.JSONDecodeError):
        return False

