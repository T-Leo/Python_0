list1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list2 = [i for i in list1 if list1.count(i) == 1]
print(list2)
