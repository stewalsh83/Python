import sys

def calc_average(numbers):
    mean = sum(numbers) / len(numbers)
    return mean

def main():
    """ Gives accumilated average from txt file """
    line = sys.stdin.readlines()
    tokens = line
    a = []
    for tok in tokens:
        a.append(int(tok))
        print(a)
        print(calc_average(a))
        print('\n')

if __name__ == "__main__":
    main()

# python3 get-average.py < numbers.txt