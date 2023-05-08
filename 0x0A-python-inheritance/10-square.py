#!/usr/bin/python3
"""Definiing a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a square (Rectangle)"""

    def __init__(self, size):
        """Initializing square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
