monthNum = int(input('enter the number of the month- '))
while monthNum > 12 or monthNum < 1:
    monthNum = int(input('enter the number of the month- '))

# print(monthNum)

monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
print('the month is- ', (monthList.pop(monthNum - 1)))

if monthNum < 3 or monthNum == 12:
    print("it'total_sum a winter")

elif monthNum > 2 and monthNum < 6:
    print("it'total_sum a spring")

elif monthNum > 5 and monthNum < 9:
    print("it'total_sum a summer")

else:
    print("it'total_sum an autumn")
