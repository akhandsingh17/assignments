from collections import defaultdict


def EmplDict(lst):
    dd = defaultdict(list)
    for rel in lst:
        for friend in rel:
            dd[friend].extend(list(x for x in rel if x not in friend))

    return {key: sum(map(lambda x: len(x), value)) for key, value in dd.items()}


lst = [['A', 'B', 'C'], ['B', 'F', 'D'], ['A', 'D'], ['E']]
print(EmplDict(lst))
