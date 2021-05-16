def div():
    a = float(input('enter the first number-'))
    b = float(input('enter the second number- '))

    if b == 0:
        return print('cannot divide by zero')
    else:
        return a / b


div_result = div()
print(div_result)
