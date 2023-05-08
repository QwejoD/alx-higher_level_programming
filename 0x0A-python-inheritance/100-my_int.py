#!/usr/bin/python3
"""Defining a class MyInt that inherits from int."""


class MyInt(int):
    """Invert"""

    def __eq__(self, value):
        """Override == """
        return self.real != value

    def __ne__(self, value):
        """Override != """
        return self.real == value
