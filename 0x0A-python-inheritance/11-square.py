#!/usr/bin/python3
"""Defining a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square(rectangle)"""

    def __init__(self, size):
        """Initializing a square.
        
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
