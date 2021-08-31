import sys


def main():
    """Displays text file in tabulated columns."""
    header = '{} {} {:>10s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format('POS', 'CLUB', 'P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'PTS')
    print(header)
    for line in sys.stdin:
        lines = line.strip().split()

        col_1 = lines[0]
        col_2 = lines[1]
        col_4 = lines[-8]
        col_5 = lines[-7]
        col_6 = lines[-6]
        col_7 = lines[-5]
        col_8 = lines[-4]
        col_9 = lines[-3]
        col_10 = lines[-2]
        col_11 = lines[-1]

        if len(lines[2]) > 2:
            col_3 = lines[2]
        else:
            col_3 = ''
        col = col_2 + ' ' + col_3
        print('{:>3s} {:<12s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format(col_1, col, col_4, col_5, col_6, col_7, col_8, col_9, col_10, col_11))


if __name__ == "__main__":
    main()