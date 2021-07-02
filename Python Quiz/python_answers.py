#!/usr/bin/env python3

# use min() to get the minimum dictionary value
def q1():
    d = {'coyote': 3,
         'elephant': 7,
         'dog': 4,
         'chimpanzee': 2,
         'deer': 8}
    print(min(d.values())) # output 2
# q1()

# use list comp to count words in list that dont include "a"
def q2():
    words = ['wound',
             'below',
             'hungry',
             'bronze',
             'subtle']
    print(len([w for w in words if 'a' not in w])) # output 5
# q2()

def q3():
    d = {'giraffe': 5,
         'dog': 4,
         'deer': 2,
         'panda': 8,
         'mole': 6}
    print(max(d.values()))
# q3()

def q4():
    words = ['confess',
             'elect',
             'arrange',
             'harvest',
             'beast',
             'tobacco']
    print(len([w for w in words if 'a' in w]))
# q4()

def q5():
    d = {'ox': 4,
         'kangaroo': 2,
         'koala': 5,
         'goat': 8,
         'squirrel': 9}
    print(min(d.keys()))
# q5()

def q6():
    d = {'lion': 7,
         'otter': 2,
         'cow': 5,
         'goat': 3,
         'squirrel': 9}
    print(len(d))
# q6()

def q7():
    words = ['aspect',
             'solar',
             'racial',
             'alive',
             'figure']
    print(len([w for w in words if len(w) < 6]))
# q7()

def q8():
    numbers = [6, 16, 20, 1, 14, 9, 19]
    print(len([n for n in numbers if n < 10]))
# q8()

def q9():
    numbers = [9, 15, 16, 5, 4, 14]
    print(len([n for n in numbers if n % 2]))
# q9()

def q10():
    numbers = [8, 4, 17, 18, 7, 6]
    print(len([n for n in numbers if n < 10]))
# q10()

def q11():
    d = {'lion': 9,
         'otter': 6,
         'panda': 1,
         'mole': 3,
         'coyote': 5,
         'kangaroo': 7}
    print(max(d.values()))
# q11()

def q12():
    numbers = [16, 14, 7, 20, 4, 9]
    print([n-1 for n in numbers])
# q12()

def q13():
    words = ['patient',
             'since',
             'control',
             'forbid',
             'await',
             'courage']
    print(len([w for w in words if len(w) > 6]))
# q13()

def q14():
    words = ['lucky',
             'light',
             'denial',
             'motion',
             'bench',
             'company',
             'devil']
    print([1 if 'e' in w else 0 for w in words])
# q14()

def q15():
    numbers = [17, 1, 4, 14, 19, 6, 18]
    print([n-1 for n in numbers])
# q15()

def q16():
    numbers = [19, 18, 14, 2, 17, 16, 4]
    print(len([n for n in numbers if n % 2]))
# q16()

