gains = float(input("enter company's gains- "))
costs = float(input("enter company's costs- "))
workers = int(input('enter the amount of workers- '))

if gains > costs:
    type('business is profitable')

    profit = float(gains - costs)
    type('profit is- ')
    type(profit)

    profitability = float(profit / gains)
    type('profitability is- ')
    type(profitability)

    profit_per_worker = profit / workers
    type('profit per worker is- ')
    type(profit_per_worker)

else:
    type('business is not profitable')
