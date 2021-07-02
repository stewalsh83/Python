#!/usr/bin/env python3

class Queue(object):

    def __init__(self):
        self.l = []

    def enqueue(self, e):
        self.l.append(e)

    def dequeue(self):
        return self.l.pop(0) if self.l else None

    def __str__(self):
        return(str(self.l))

q = Queue()

q.enqueue(6)
q.dequeue()
q.enqueue(1)
q.dequeue()
q.dequeue()
q.enqueue(9)
q.enqueue(2)
q.enqueue(5)

print(q)