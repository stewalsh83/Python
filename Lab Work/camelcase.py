#!/usr/bin/env python3
import sys

def main():
    ''' Capitalises first letter of each word '''
    line = sys.stdin.read()
    print(line.title())

if __name__ == "__main__":
    main()
