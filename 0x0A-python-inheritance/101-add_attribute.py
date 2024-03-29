#!/usr/bin/python3
"""Defining a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Adds new attribute to an object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
