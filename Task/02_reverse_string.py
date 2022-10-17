#!/usr/bin/env python3


def reverse_string(s):
    '''Reverses a string iteratively'''
    t = ""
    i = 0

    while i < len(s):
        # iterates the last letter in s and assigns it to t
        t += s[len(s) - i - 1]
        i += 1
    return t


def recursive_reverse(s):
    '''Reverses a string recursively'''
    # Base case
    if s == "":
        return s
    # Recursive case
    else:
        # s[1:] removes first char from a string and outputs remaining string
        return recursive_reverse(s[1:]) + s[0]
