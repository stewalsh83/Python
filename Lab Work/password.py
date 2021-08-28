#!/usr/bin/env python3
import sys


def password(lines: str) -> None:
    """
    Counts how many different characters classes are in a password.
    """
    dig, low, cap, s_char = 0, 0, 0, 0
    special = "^@()$¬!£%&*{}[]?/.,<>"

    i = 0
    while i < len(lines):
        if lines[i].isdigit():
            dig = 1
        if lines[i].islower():
            low = 1
        if lines[i].isupper():
            cap = 1
        if lines[i] == special[i]:
            s_char = 1
        i += 1
    print(dig + low + cap + s_char)


def main():
    for line in sys.stdin:
        lines = line.strip()
        password(lines)


if __name__ == "__main__":
    main()
