#!/usr/bin/env python3
import sys


def main():
    """Checks if letters from 1st word are contained in 2nd word."""
    for line in sys.stdin:
        [word1, word2] = line.lower().strip().split()
        char1 = ''.join(sorted(word1))
        char2 = ''.join(sorted(word2))

        if char1 in char2:
            print(True)
        else:
            print(False)


if __name__ == "__main__":
    main()
