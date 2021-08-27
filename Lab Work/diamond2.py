#!/usr/bin/env python3
import sys

def diamond(line):
    '''Makes a diamond and determines
    the size from each number in file'''
    n = ' *'
    m = ' '
    count1 = 0
    count2 = line

    i = 0
    while i < line:
        count1 += 1
        count2 -= 1
        print(m * count2 + n * count1)
        i += 1

    j = count1
    while j > line - line:
        count1 -= 1
        count2 += 1
        print(m * count2 + n * count1)
        j -= 1
    print('', end='')

def main():
    for line in sys.stdin:
        line = line.rstrip()
        line = int(line)

        diamond(line)

if __name__ == "__main__":
    main()
