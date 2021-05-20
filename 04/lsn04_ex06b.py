from itertools import cycle

lst = [22, 123, 5123, 22222244, 99, 00, True]
cnt = 0

for i in cycle(lst):
    print(i)
    cnt += 1
    if cnt == 100:
        break
