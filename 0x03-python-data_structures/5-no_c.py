#!/usr/bin/env python3
#5-no_c.py


def no_c(my_string):
    """Remove all characters c and C from a string."""
    copy = [d for d in my_string if d != 'c' and d != 'C']
    return ("".join(copy))
