scndsX = int(input('enter the amount of seconds- '))
hrsX = int(scndsX // 3600)
mnts = int((scndsX % 3600) // 60)
scnds = int(scndsX % 60)

print('total amount of time is:')
print(hrsX, ':', mnts, ':', scnds)
