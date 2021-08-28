#!/usr/bin/env python3
import sys


def trim(fname, lname):
    """Extracts first and last name from dcu email addresses."""
    i = 0
    while i < len(lname):
        if lname[i].isdigit():
            lname = str(lname[0:i])
        i = i + 1
    print(fname.title(), lname.title())


def main():
    for line in sys.stdin:
        line = line[:-12]
        fname, lname = line.split('.')

        trim(fname, lname)


if __name__ == "__main__":
    main()
