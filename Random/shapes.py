# Pattern
#for s in range(9):
#   print('*')
print('\n')
#s = int(input('Enter Number for Square : '))
s = 4
i = 0
while i < s:
   t = '* ' * s
   print(t)
   i += 1
print('\n')
#------------------------------------------------------------------------------------------------
for i in range(s):
   for j in range(s):
      print('$', end=' ')
   print()
print('\n')
#------------------------------------------------------------------------------------------------
# right triangle 1
num = 5
for i in range(num + 1):
   print('* ' * i)
print('\n')
#------------------------------------------------------------------------------------------------
# right triangle 2
num = 5
for i in range(1, num + 1):
   print('  ' * (num - i) + '* ' * i) # added double space '  ' to allow for '* '
# formula : ' ' * (num - i) white space * 5 - index
# + '*' * i for shape
# note '* ' will give triangle
print('\n')
#------------------------------------------------------------------------------------------------
# right triangle 3
num = 5
for i in range(num, 0, - 1):
   print('  ' * (num - i) + '* ' * i)
print('\n')
#------------------------------------------------------------------------------------------------
# right triangle 4
num = 5
for i in range(num, 0, - 1):
   print('* ' * i)
print('\n')
#------------------------------------------------------------------------------------------------
# triangle
num = 5
for i in range(1, num + 1):
   print(' ' * (num - i) + '* ' * i)
print('\n')
#------------------------------------------------------------------------------------------------
# upside down triangle
for i in range(num, 0, -1):
   print(' ' * (num - i) + '* ' * i)
print('\n')
#----------------------------------------------------------------------------------------
# dimond
num = 5
for i in range(1, num + 1):
   print(' ' * (num - i) + '* ' * i)
for i in range(num - 1, 0, -1):
   print(' ' * (num - i) + '* ' * i)
# num - 1 to remove simular row
#------------------------------------------------------------------------------------------------
print('\n')
# right arrow : RTri 1 and 4
num = 5
for i in range(num + 1):
   print('* ' * i)
for i in range(num-1, 0, - 1):
   print('* ' * i)
print('\n')
#--------------------------------------------------------------------------------------------------------
# left arrow : Rtri 2 and 3
num = 5
for i in range(1, num + 1):
   print('  ' * (num - i) + '* ' * i)
for i in range(num-1, 0, - 1):
   print('  ' * (num - i) + '* ' * i)
print('\n')
#-----------------------------------------------------------------------------------------------------------
# hour glass
num = 7
for i in range(num, 1, -1):
   print(' ' * (num - i) + ' *' * i)
for i in range(1, num + 1):
   print(' ' * (num - i) + ' *' * i)
print('\n')
#---------------------------------------------------------------------------------------------------------
# mixed square
for i in range(1, num + 1):
   print('$ ' * (num - i) + ' *' * i)
#---------------------------------------------------------------------------------------------------------
print('\n')
# mixed square 2
o = 7
for i in range(1, o + 1):
   o1 = '$ ' * (o - i) + '* ' * i
   o2 = '  ' * (o - i) + '* ' * i
   print('- {:>10s}{} -'.format(o1, o2))
for i in range(1, o):
   o3 = '$ ' * (o - i) + '* ' * i
   o4 = '* ' * (o - i) + '$ ' * i
   print('- {:>10s}{} -'.format(o4, o3))
print('\n')
#------------------------------------------------------------------------------------------------------------------
# dimond x3
d = 7
for i in range(1, d + 1):
   d1 = ' ' * (d - i) + '* ' * i
   print(' {:>5} . {:>15} . {:>15} .'.format(d1, d1, d1))
for i in range(d - 1, 0, -1):
   d2 = ' ' * (d - i) + '* ' * i
   print(' {:>5} . {:>15} . {:>15} .'.format(d2, d2, d2))
print('\n')
#------------------------------------------------------------------------------------------------
num = 5
for i in range(num):
   for j in range(num):
      print('*', end=' ')
   print()
print('\n')


# Heart
# table rows/cols
#   0 1 2 3 4 5 6
# 0   * *   * *
# 1 *     *     *
# 2 *           *
# 3   *       *
# 4     *   *
# 5       *
# Output 6 rows & 7 cols
# Two for loops (nested)
# 1st loop row / 2nd loop col
# in range mention num of rows & cols
# if else conditions to control shape
# divide output into 4 parts
# row 0 (0,1 0,2 0,4 0,5) / empty col values 0 3 6
# row 1 (1,1 1,3 1,6) / oppisit of row 0
# part 3 (2,0 3,1 4,2 5,3) subtract row from col get 2, 2, 2, 2
# part 4 (2,6 3,5 4,4)
# row looking at empty col values
# not = 0 add '*' using mod %
# 0%3=0 3%3=0 6%3=0

for row in range(6):
   for col in range(7):
      if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
         print('\u001b[31m* \u001b[37m', end='')
      else:
         print('  ', end='')
   print() # for new line
print('\n')
#--------------------------------------------------------------------------------------------------
#   0 1 2 3 4 5 6
# 0 *           *
# 1   *       *
# 2     *   *
# 3       *
# 4     *   *
# 5   *       *
# 6 *           *
# Output 7 rows & 7 cols
# conditions
# row col ---- row col
#   0 0          0 6
#   1 1          1 5
#   2 2          2 4
#   3 3          4 2
#   4 4          5 1
#   5 5          6 0
#   6 6

for row in range(7):
   for col in range(7):
      if (row == col) or (row + col == 6):
         print('* ', end='')
      else:
         print('  ', end='')
   print()
print('\n')
#-----------------------------------------------------------------------------------------
#   0 1 2 3 4 5 6
# 0       *
# 1     *   *
# 2   *       *
# 3 *     *     *
# 4   *       *
# 5     *   *
# 6       *
# Output 7 rows & 7 cols
# conditions
# row col ---- row col
#   0+3          1-4
#   1+2          2-5
#   2+1          3-6
#   3+0
# row col      row col
#                4-1
#   4,5   ----   5-2
#   5,4          6-3
#
#   3%3
print('\u001b[42m')
print('\u001b[40m')
print('\n')
for row in range(7):
   for col in range(7):
      if (row + col == 3) or (row - col == 3) or (row - col == -3) or (row + col == 9) or (row == 3 and col % 3 == 0):
         print('\u001b[34m* \u001b[37m', end='')
      else:
         print('* ', end='')
   print()
print('\n')
#--------------------------------------------------------------------------------------------------
# conditions based on finding common values!!!
#   0 1 2 3 4 5 6 7 8 9
# 0
# 1     *         *
# 2       *     *
# 3     * * * * * *
# 4   * *   * *   * *
# 5 * * * * * * * * * *
# 6 *   * * * * * *   *
# 7 *   *         *   *
# 8       * * * *
# 9
# Output 10 rows & 10 cols
# conditions
# row col
#   1,2 1,7
for row in range(10):
   for col in range(10):
      if (row and col == 11):
         print('* ', end='')
      elif (row == 1 and row + col == 3) or (row == 1 and row - col == -6):
         print('* ', end='')
      elif (row == 2 and row + col == 5) or (row == 2 and row + col == 8):
         print('* ', end='')
      elif (row == 3 and row + col >= 5 or row + col > 11):
         print('* ', end='')
      elif (row == 5):
         print('* ', end='')
      else:
         print('. ', end='')
   print()
print('\n')


# ansi colors
# text
# Red \u001b[31m
# Blue \u001b[34m
# White \u001b[37m

# background
# Green \u001b[42m
# Black \u001b[40m
#      BG Green   TXT red         TXT Blue        TXT White  BG Black
print('\u001b[42m \u001b[31mHello \u001b[34mWorld \u001b[37m \u001b[40m')
print('\n')

# 256 color backgrounds
import sys
for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write(code.ljust(5))
    print()
print('\n')
import sys
for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
    print(u"\u001b[0m")
print('\n')
# grid 1 to 100
for i in range(0, 10):
   for j in range(1, 11):
      formula = str(i * 10 + j)
      sys.stdout.write('\u001b[7m' + formula.ljust(5))
   print()
print('\n')

# bold \u001b[1m
# underline \u001b[4m
# reversed \u001b[7m
print('\u001b[40mhello')