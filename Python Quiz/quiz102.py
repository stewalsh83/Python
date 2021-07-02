#!/usr/bin/env python3

class X(object):

    def __init__(self, x):
        self.x = x

    def __sub__(self, other):
        t = self.x
        for c in other.x:
            if c in t:
                t = t.replace(c, '')
        return X(t)

    def __str__(self):
        return(self.x)

p = X('aef')
q = X('cfge')
r = p - q

print(r)