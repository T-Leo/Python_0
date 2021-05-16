# def my_func(a, b, sum_x):
#     return a + b + sum_x - min(a, b, sum_x)


my_func = lambda a, b, c: a + b + c - min(a, b, c)


sum_max = my_func(float(input('enter the first number- ')),
                  float(input('enter the second number- ')),
                  float(input('enter the third number- ')))
print(sum_max)
