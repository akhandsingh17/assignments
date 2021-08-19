### Given a list of ints, balance the list so that each int appears equally in the list.
# Return a dictionary where the key is the int and the value is the count needed to balance the list.
"""
[1, 1, 2] => {2: 1}

[1, 1, 1, 5, 3, 2, 2] => {5: 2, 3: 2, 2: 1}

"""

def balance_list(lst):
    count = {}
    for num in lst:
        count[num] = count.get(num, 0) + 1
    max_kv = max(count.items(), key = lambda x:x[1])

    count.pop(max_kv[0], None)
    for key, val in count.items():
        count[key] = max_kv[1] - count.get(key)
    return count

assert balance_list([1, 1, 2]) == {2: 1}
assert balance_list([1, 1, 1, 5, 3, 2, 2]) == {5: 2, 3: 2, 2: 1}
