#!/usr/bin/python3

"""Addition function for integer definition."""


def add_integer(a, b=98):
    """Function returns the addition of a and b.
    Float args are typecasted to ints before addition is performed.
    Raises:
        TypeError: a and b must be integers.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
