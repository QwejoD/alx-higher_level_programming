#!/usr/bin/python3
"""a class Rectangle that defines a rectangle
"""


class Rectangle:
    """Represents a Polygon with opposite sides equal."""
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle with a given width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of this Rectangle.

        """
        return self.__width

    @property
    def height(self):
        """Retrieves the height of this Rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Update the width of this Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Update the height of this Rectangle
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
