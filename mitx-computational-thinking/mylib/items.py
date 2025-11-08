import random

class Item(object):
    def __init__(self, n, w, v):
        self._name = n
        self._value = v
        self._weight = w

    def get_name(self):   return self._name
    def get_value(self):  return self._value
    def get_weight(self): return self._weight

    def __str__(self):
        return '\n{:>15}: <value: {:>3}, weight: {:>3}>'.format(
            self._name, self._value, self._weight)

    __repr__ = __str__


def build_items():
    names   = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values  = [175,      90,         20,     50,    10,     200]
    weights = [10,       9,          4,      2,     1,      20]
    items = []
    for i in range(len(values)):
        items.append(Item(names[i], weights[i], values[i]))
    return items


def build_many_items(num_items, max_val, max_weight):
    items = []
    for i in range(num_items):
        items.append(
            Item(str(i),
            random.randint(1, max_val),
            random.randint(1, max_weight)
            )
        )
    return items
