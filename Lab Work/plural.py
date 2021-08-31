import sys


def main():
    """Turns a noun into a plural"""
    p = ['es', 'ies', 'ves', 's']
    for i in sys.stdin:
        line = i.strip()
        last = line[-1]
        sec_last = line[-2:]

        if 'ch' in sec_last or 'sh' in sec_last:
            print(line + p[0])
        elif 'o' in last or 'x' in last or 'z' in last or 's' in last:
            print(line + p[0])
        elif 'fe' in sec_last:
            print(line[:-2] + p[2])
        elif 'f' in last:
            print(line[:-1] + p[2])
        elif 'ty' in line:
            print(line[:-1] + p[1])
        else:
            print(line + p[3])


if __name__ == "__main__":
    main()
