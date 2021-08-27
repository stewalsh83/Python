import sys

def main():
    for line in sys.stdin:
        num, base = line.strip().split()
        convert = int(num, int(base))
        print(convert)

if __name__ == "__main__":
    main()
