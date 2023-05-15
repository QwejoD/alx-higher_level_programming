#!/usr/bin/python3
"""a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes
"""
class LockedClass:

    __slots__ = "first_name"
