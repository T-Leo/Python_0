a = []
b = int(input("enter the total amount of contents- "))

for i in range(b):
    a.append(input("enter the list's contents- "))
print(a)

d = 1
while d < b:
    c = a.pop(d)
    # print(num_a)
    a.insert(d - 1, c)
    # print(num_a)
    d = d + 2

print(a)
