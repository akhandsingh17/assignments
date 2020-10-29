"""
Suppose you have a dic

{'a': 1,
 'c': {'a': 2,
       'b': {'x': 5,
             'y' : 10}},
 'd': [1, 2, 3]}

 You want to flatten the dic

 {'a': 1,
 'c_a': 2,
 'c_b_x': 5,
 'c_b_y': 10,
 'd': [1, 2, 3]}

"""

x = {'a': 1,
     'c': {'a': 2,
           'b': {'x': 5,
                 'y' : 10}},
     'd': [1, 2, 3]}

from collections import MutableMapping
def flatten(d, parent_key = '', seperator = '_'):
    items = []
    for k , v in d.items():
        new_key = parent_key + seperator + k if parent_key else k
        if isinstance(v, MutableMapping):
            items.extend(flatten(v, new_key, seperator = seperator).items())
        else:
            items.append((new_key, v))
    return dict(items)


print(flatten(x))

