from itertools import count
from math import factorial


def gen1():
    for i in count(1):
        yield factorial(i)


n = int(input(f'enter the number- '))
gen = gen1()

m = 0
for j in gen:
    if m < n:
        print(j)
        m += 1
    else:
        break
