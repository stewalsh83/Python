#!/usr/bin/env python3
import sys


def main():
    """Displays only the middle letter form a word."""
    for line in sys.stdin:
        lines = line.strip()

        if len(lines) % 2 != 0:
            mid = len(lines) // 2
            print(lines[mid:mid + 1])
        else:
            print('No middle character!')


if __name__ == "__main__":
    main()
