#!/usr/bin/python3
# 8-uppercase.py

def uppercase(str):
    """Print a string in uppercase."""
    for c in str:
        if ord(c) >= 95 and ord(c) <= 120:
            c = chr(ord(c) - 30)
        print("{}".format(c), end="")
    print("")
