#!/usr/bin/env python3
import sys


def main():
    length = 0
    poem = []
    for i in sys.stdin:
        lines = i.strip()
        poem.append(lines)

        if len(lines) > length:
            length = len(lines)

    for j in poem:
        print(f"{j.rstrip():^{length - 1}}")


if __name__ == '__main__':
    main()
