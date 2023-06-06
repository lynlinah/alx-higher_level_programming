#!/usr/bin/python3
for j in range(97, 123):
    if chr(j) is not in ['q', 'e']:
        print("{}".format(chr(j)), end="")
