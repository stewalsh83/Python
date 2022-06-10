import sys

def calc():
	""" calculate excel colums into a single value """
	line = sys.stdin
	for i in line:
		n = i.strip().split()

		col1 = int(n[0]) * (-1)
		col2 = int(n[1]) * (-1)
		col3 = int(n[2]) * 1
		col4 = int(n[3]) * (-0.5)
		col5 = int(n[4]) * (-0.5)
		col6 = int(n[5]) * (-0.5) # FL + -
		col7 = int(n[6]) * 1.5
		col8 = int(n[7]) * (3)
		col9 = int(n[8]) * (-1.5)
		col10 = int(n[9]) * (-3)

		print(col1 + col2 + col3 + col4 + col5 + col6 + col7 + col8 + col9 + col10)

calc()

# calc-nums.py < nums.txt
