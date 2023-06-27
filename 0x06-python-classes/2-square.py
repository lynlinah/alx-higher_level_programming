#!/usr/bin/python3
"""class Square that defines a square"""


class Square():
    """class square with it's size and proper validation"""

    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an int")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size