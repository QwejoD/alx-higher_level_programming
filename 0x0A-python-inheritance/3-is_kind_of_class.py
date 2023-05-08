#!/usr/bin/python3
"""Defining a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.
    return True if it is and false if it isnt.
    """
    if isinstance(obj, a_class):
        return True
    return False
