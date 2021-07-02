#!/usr/bin/env python3

import sys

def diamond(n):
   i = 1
   while i < n:
      d = (" " * (n - i) + "* " * i).rstrip()
      print(d)
      i += 1
   while i > 0:
      d = (" " * (n - i) + "* " * i).rstrip()
      print(d)
      i -= 1

def main():
   n = int(sys.argv[1])
   (diamond(n))

if __name__ == "__main__":
   main()

















