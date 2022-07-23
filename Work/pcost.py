# pcost.py
#
# Exercise 1.27

totalCost = 0

with open('Data/portfolio.csv', 'rt') as file:
    next(file)
    for line in file:
        list = line.split(',')
        price = float(list[2])
        shares = int(list[1])
        totalCost += price * shares

print(f"Total cost is ${totalCost}")
