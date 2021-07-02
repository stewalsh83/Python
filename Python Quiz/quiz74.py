#!/usr/bin/env python3

class Stack(object):

    def __init__(self):
        self.l = []

    def push(self, e):
        self.l.append(e)

    def pop(self):
        return self.l.pop() if self.l else None

    def __str__(self):
        return(str(self.l))

s = Stack()

s.push(6)
s.pop()
s.push(2)
s.push(7)
s.push(3)
s.pop()

print(s)