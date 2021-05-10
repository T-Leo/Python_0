a = float(input('enter the first distance- '))
b = float(input('enter the last distance- '))
c = 0

while a < b:
    print('Day', c, ':', a)
    a = a * 1.1
    c = c + 1

print('On the day #', c, 'the distance is more than', b)
