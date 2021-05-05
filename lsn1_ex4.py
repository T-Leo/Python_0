a = int(input('enter the positive number- '))

while a <= 0:
    a = int(input('enter the positive number- '))
    if a > 0:
        continue

s = str(a)
ls = list(map(int, s))
r = max(ls)
print(r)
