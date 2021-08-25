import sys

def main():
    '''Reads text file and capitalizes the first and last letters'''
    for line in sys.stdin:
        lines = line.strip()

        first = lines[0].upper()
        last = lines[-1].upper()
        mid = lines[1:-1]

        caps = first + mid + last
        if first != last:
            print(caps)

if __name__ == "__main__":
    main()