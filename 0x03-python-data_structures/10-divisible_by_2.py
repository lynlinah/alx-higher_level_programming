#!/usr/bin/python3
# 10-divisible_by_2.py


def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    result = []
    for k in range(len(my_list)):
        if my_list[k] % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    return (result)
