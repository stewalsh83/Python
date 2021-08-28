#!/usr/bin/env python3
import sys


def main():
    """Removes first and last letters from strings in text file."""
    a = []
    for line in sys.stdin:
        words = line.strip()
        chopped = words[1:-1]
        a.append(chopped)
        lst = '\n'.join(a).split()
    print('\n'.join(lst))


if __name__ == "__main__":
    main()
