from functools import reduce


def fn(num_a, num_b):
    return num_a * num_b


print(f'even numbers- {[i for i in range(99, 1001) if i % 2 == 0]}')
print(f'even numbers multiplied- {reduce(fn, [j for j in range(99, 1001) if j % 2 == 0])}')
