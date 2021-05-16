def my_func():
    x = float(input('enter positive number- '))
    y = int(input('enter negative integer- '))
    if x <= 0 or y >= 0:
        return print('incorrect values')
    return x ** y


invol = my_func()
print(invol)
