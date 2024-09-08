#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a JSON to Python data structure function."""
import json


def from_json_string(my_str):
    """Return the object rep of a JSON string."""
    return json.loads(my_str)
