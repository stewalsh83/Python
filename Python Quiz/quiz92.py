#!/usr/bin/env python3

def foo(l):
    q = []
    for e in l:
        try:
            q.append(e % 2)
        except:
            q.append('A')
        finally:
            q.append('B')

    return q

print(foo([8, 'X', 4]))