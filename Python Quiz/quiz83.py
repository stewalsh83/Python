#!/usr/bin/env python3

def foo(l):
    q = []
    try:
        for i in l:
            q.append(i+1)
    except:
        q.append('A')
    else:
        q.append('B')
    finally:
        q.append('C')

    return q

print(foo(['X', 5, 9, 1, 3, 'X']))