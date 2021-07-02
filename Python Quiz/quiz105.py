#!/usr/bin/env python3

def arithmetic(p, q=0, r=2, s=1):
    return p + q + r + s

try:
    print(arithmetic(0, 1))
except:
    print('error')