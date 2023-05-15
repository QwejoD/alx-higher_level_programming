#!/usr/bin/python3
"""a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes
"""


class LockedClass:
    """locked class"""

    __slots__ = "first_name"
