gains = float(input("enter company's gains- "))
costs = float(input("enter company's costs- "))
workers = int(input('enter the amount of workers- '))

if gains > costs:
    print('business is profitable')

    profit = float(gains - costs)
    print('profit is- ')
    print(profit)

    profitability = float(profit / gains)
    print('profitability is- ')
    print(profitability)

    profit_per_worker = profit / workers
    print('profit per worker is- ')
    print(profit_per_worker)

else:
    print('business is not profitable')
