import itertools
lst=[(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),(7, 8), (9, 10)]
print(list(itertools.chain(*lst)))
flatten = [item for items in lst for item in items]
print(flatten)