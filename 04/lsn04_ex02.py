list1 = [2, 5, 12, 1231, 21, 780, 44]
list2 = [i for j, i in enumerate(list1) if list1[j - 1] < list1[j]]
print(f'first list- {list1}')
print(f'new list- {list2}')
