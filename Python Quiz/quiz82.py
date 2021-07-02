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

q.dequeue()
q.enqueue(2)
q.dequeue()
q.enqueue(5)
q.dequeue()
q.enqueue(4)
q.enqueue(3)
q.enqueue(1)

print(q)