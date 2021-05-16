total_sum = 0

try:
    while True:
        for number in map(float, input('enter the numbers- ').split()):
            total_sum += number
        print(total_sum)
except ValueError:
    print(total_sum)
