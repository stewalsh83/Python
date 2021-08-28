#!/usr/bin/env python3
import sys


def main():
    """
    +   Prints measurements of a sphere to a table
    +   from radius. Also uses data to determine
    +   increment and range of table.
    """
    for line in sys.stdin:
        numbers = line.strip().split()
        start_r = float(numbers[0])
        inc_r = float(numbers[1])
        end_r = float(numbers[2])

        h1 = 'Radius (m)'
        h4 = '-' * len(h1)
        h2 = 'Area (m^2)'
        h5 = '-' * len(h2)
        h3 = 'Volume (m^3)'
        h6 = '-' * len(h3)

        print(f'\n{h1:>s} {h2:>15s} {h3:>15s}')
        print(f'{h4:>s} {h5:>15s} {h6:>15s}')

        pi = 3.14
        radius = start_r

        while radius <= end_r:
            area = 4 * pi * radius ** 2
            volume = 4 / 3 * pi * radius ** 3
            print('{:>4.1f} {:>18.2f} {:>14.2f}'
                  .format(radius, area, volume))
            radius += inc_r


if __name__ == '__main__':
    main()
