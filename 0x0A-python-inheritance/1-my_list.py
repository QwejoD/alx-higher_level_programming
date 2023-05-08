#!/usr/bin/python3
"""
A class MyList that inherits from list
"""


class MyList(list):
    """The class implement sorted printing for the built-in list class"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
