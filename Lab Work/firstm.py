#!/usr/bin/env python3
import sys


def main():
    """The first lower case m on each line is capitalised."""
    for line in sys.stdin:
        lines = line.strip()

        lines = lines[:27] + 'M' + lines[28:]
        print(lines)


if __name__ == "__main__":
    main()
