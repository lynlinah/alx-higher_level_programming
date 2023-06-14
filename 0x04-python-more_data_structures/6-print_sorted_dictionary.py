#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys."""
     list_ord = list(a_dictionary.keys())
    list_ord.sort()
    for j in list_ord:
        print("{}: {}".format(j, a_dictionary.get(j)))
