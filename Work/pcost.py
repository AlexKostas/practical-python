# pcost.py
#
# Exercise 1.27

import csv


def portfolio_cost(filename):

    totalCost = 0

    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            price = float(row[2])
            try:
                shares = int(row[1])
            except ValueError:
                print("Warning: error parsing line!")
                continue
            totalCost += price * shares

    return totalCost


totalCost = portfolio_cost('Data/missing.csv')
print(f"Total cost is ${totalCost}")
