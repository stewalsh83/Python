#!/usr/bin/env python3

class X(object):

    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        t = self.x
        for c in other.x:
            if c not in t:
                t += c
        return X(t)

    def __str__(self):
        return(self.x)

p = X('gdb')
q = X('egbd')
r = p + q

print(r)