def my_func():
    x = float(input('enter positive number- '))
    y = int(input('enter negative integer- '))
    if x <= 0 or y >= 0:
        return print('incorrect values')
    for i in range(abs(y) - 1):
        x = x * x
    return 1 / x


invol = my_func()
print(invol)
