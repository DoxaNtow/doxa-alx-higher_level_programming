#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Initialize, get, and set dimensions.

    Args:
        width (int): Rectangle width.
        height (int): Rectangle height.
    """

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width.

        Args:
            value (int): New width.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height.

        Args:
            value (int): New height.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter, or 0 if either dimension is 0."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
