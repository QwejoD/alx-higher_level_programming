#!/usr/bin/python3
"""a function that returns the list of available attributes and methods of an object"""


def lookup(obj):
    """Returns a list of an object available attributes using 'dir'."""
    return (dir(obj))
