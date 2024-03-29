#!/usr/bin/python3
"""Defining a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle BaseGeometry."""

    def __init__(self, width, height):
        """Intialize rectangle 
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return area"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str()"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
