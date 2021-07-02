#!/usr/bin/env python3

def arithmetic(p, q=1, r=2, s=0):
    return p + q + r + s

try:
    print(arithmetic())
except:
    print('error')