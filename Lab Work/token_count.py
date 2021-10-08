import sys


def main():
    token = sys.stdin.read().strip().lower().split()
    token = sorted(token)
    print(len(token))


if __name__ == "__main__":
    main()
