#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" For-in Strings

For-in strings can be used to iterate through each character in a string.

"""

to_reverse = input("Enter anything, this program will reverse it: ")

backwards = ""
for character in to_reverse:
    backwards = character + backwards

print("end of program")
print(backwards)
