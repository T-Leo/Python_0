a = int(input('enter the positive number- '))

while a <= 0:
    a = int(input('enter the positive number- '))
    if a > 0:
        continue

maX = a % 10
num = a

while num > 0:
    digit = num % 10
    if digit > maX:
        maX = digit
        if digit == 9:
            break

    num = num // 10
    print(num)

print('the biggest digit is- ', maX)
