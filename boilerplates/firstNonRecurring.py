from collections import defaultdict

def firstNonRecurring(lst):
    """
    get the first non recurring integer from the list. Time complexity should be O(n)
    :param lst:
    :return:
    """
    mp = defaultdict(lambda: 0)
    # Insert all array elements in hash table
    for i in range(len(lst)):
        mp[lst[i]] += 1

    # Traverse array again and return
    # first element with count 1.
    for i in range(len(lst)):
        if mp[lst[i]] == 1:
            return lst[i]
    return -1

if __name__ == "__main__":
    assert firstNonRecurring([]) == -1
    assert (firstNonRecurring([1, 2, 1])) == 2
    assert (firstNonRecurring([1, 2, 1, 3, 2])) == 3
    assert (firstNonRecurring([1, 2, 1, 3, 3, 4])) == 2
    assert (firstNonRecurring([1, 2, 1, 2])) == -1