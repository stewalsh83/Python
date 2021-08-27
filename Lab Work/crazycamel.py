#!/usr/bin/env python3
import sys

def main():
    ''' Capitalises last letter of each word '''
    line = sys.stdin.read()
    reverse = line[::-1].title()
    print(reverse[::-1])

if __name__ == "__main__":
    main()
