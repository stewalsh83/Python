#!/usr/bin/env python3
import sys


def main():
    """Checks for anagram between two words on the same line"""
    for i in sys.stdin:
        lines = i.strip().split()
        token_1, token_2 = lines[0], lines[1]

        s = sorted(token_1)
        t = sorted(token_2)

        if s == t:
            print(True)
        else:
            print(False)


if __name__ == "__main__":
    main()
