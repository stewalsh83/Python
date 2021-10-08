#!/usr/bin/env python3
import sys


# def even(s):
#     if len(s) % 2 == 0:
#         start = s[:len(s) // 2]
#         end = s[len(s) // 2:]
#         end = end[::-1]
#
#         if start == end:
#             print(True)
#         else:
#             print(False)


# def odd(s):
#     if len(s) % 2 != 0:
#         start = s[:len(s) // 2]
#         end = s[len(s) // 2:]
#         end = end[1:]
#         end = end[::-1]
#
#         if start == end:
#             print(True)
#         else:
#             print(False)


def main():
    for i in sys.stdin:
        lines = i.strip()

        s = ''.join(filter(str.isalnum, lines))
        s = s.lower()
        print(s == s[::-1])

        #even(s)
        #odd(s)


if __name__ == "__main__":
    main()
