#!/usr/bin/python3
"""Defining class Square."""


class Square:
    """Representing a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): Integer size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size of integer type")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return (self.__size * self.__size)
