class Stack(object):

    def __init__(self):
        self.l = []

    def push(self, e):
        """Insert an item to the stack."""
        self.l.append(e)

    def pop(self):
        """Remove and return the last added item from the stack."""
        return self.l.pop()

    def top(self):
        """Returns whats on top of the stack."""
        return self.l[-1]

    def bottom(self):
        """Returns whats at the bottom of the stack."""
        return self.l[0]

    def is_empty(self):
        """Checks if the stack is empty and returns boolean"""
        return len(self.l) == 0

    def size(self):
        """The number of items in the stack."""
        return len(self.l)

    def __len__(self):
        """Return length of the stack."""
        return len(self.l)

    def __iter__(self):
        """Return iterator for the stack."""
        for x in self.l:
            yield x

    # deals with <__main__.Stack object at memory address>
    def __str__(self):
        """String representation of the stack."""
        return "".join([str(l) for l in self])


if __name__ == "__main__":
    s = Stack()
    s.push('A')
    s.push('B')
    s.push('C')
    s.push('D')
    n = s.pop()
    m = s.pop()
    s.push(n)
    s.push(n)
    n = s.pop()

    print("Stack =", s)
    print("Size =", s.size())
    print(len(s))
    print("Top of Stack =", s.top())
    print("Is the Stack empty =", s.is_empty())
    print("Bottom of Stack =", s.bottom())
    print(str(s))

# s = []
# s.append('A')
# s.append('B')
# s.append('C')
# s.append('D')
# n = s.pop()
# m = s.pop()
# s.append(n)
# s.append(n)
# n = s.pop()
# print(s)
