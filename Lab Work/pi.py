import math
import sys


def pi(line: int) -> None:
    """Uses custom precision on pi"""
    pi = math.pi
    if line != 0:
        print(f'{pi:,.{line}f}')


def main():
    for i in sys.stdin:
        line = i.strip()
        pi(line)


if __name__ == "__main__":
    main()
