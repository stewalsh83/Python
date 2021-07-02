import sys

def rev_list():
	''' Reverses any list from the command line '''
	args = sys.argv[1:]

	for i in args:
		lst = list(args)

	print("Your reversed list is {:>8} {}\n".format("", lst[::-1]))

def main():
	rev_list()

if __name__ == "__main__":
	main()