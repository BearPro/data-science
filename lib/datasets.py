import json
from functools import reduce

from numpy import fabs

def skip(n, items):
    counter = 0
    for i in items:
        if counter >= n:
            yield i
        else:
            counter += 1

def from_json(path):
    with open(path, 'r') as file:
        return json.load(file)

def from_csv(path):
    def add_item(xs, x):
        tx_number = int(x[0]) - 1
        tx_value = x[1].strip()
        if tx_number in xs.keys():
            xs[tx_number].add(tx_value)
        else:
            xs[tx_number] = set([tx_value])
        return xs

    with open(path, 'r') as file:
        return reduce(
            add_item,
            map(
                lambda x: x.split(',')[2:], 
                skip(1, file)),
            {}
        ).values()

if __name__ == "__main__":
    from_csv("./data/BreadBasket_DMS.csv")

