#!/usr/bin/env python3
import sys


def main():
    """Reads text file and checks if word1 exists in word2."""
    for line in sys.stdin:
        lines = line.lower().strip().split()
        word1 = lines[0]
        word2 = lines[1]

        if word1 in word2:
            print(True)
        else:
            print(False)


if __name__ == "__main__":
    main()
