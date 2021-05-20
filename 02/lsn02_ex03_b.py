monthNum = int(input('enter the number of the month- '))
while monthNum > 12 or monthNum < 1:
    monthNum = int(input('enter the number of the month- '))

# print(monthNum)

monthDict = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
print('the month is- ', (monthDict.get(monthNum)))

if monthNum < 3 or monthNum == 12:
    print("it's num_a winter")

elif monthNum > 2 and monthNum < 6:
    print("it's num_a spring")

elif monthNum > 5 and monthNum < 9:
    print("it's num_a summer")

else:
    print("it's an autumn")
