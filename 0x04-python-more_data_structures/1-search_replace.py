#!/usr/bin/python3
#1-search_replace.py

def search_replace(my_list, search, replace):
    """ Replace all occurrences of an element by another in a new list."""
    new_list = []

    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)

            return(new_list)
