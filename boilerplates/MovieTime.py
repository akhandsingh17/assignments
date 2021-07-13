
def MovieTimes(lst):
    """
    Find the total time for which movie has been watched.
    Tuple represents movie start and end time and there are overlapping intervals

    :param tup:
    :return:

    1) Empty List => [0,0]
    2) Not Sorted based on start time.I have to Sort (lst[0][0])
     [(0, 10),  (12, 20),(15, 25), (30, 48)]   ==> [(0,10),(12,25),(30,48)]   => 10+13+18
    3) Overlap => yes , No

    """
    """
     Find the total time for which movie has been watched. Tuple represents movie start and end time and
     there are overlapping intervals
     :param tup:
     :return:
     """
    lst = sorted(lst, key=lambda x: x[0])
    result = [lst[0]]
    k = 0
    for i in range(1, len(lst)):
        if result[k][1] > lst[i][0]:
            temp = (result[k][0], lst[i][1])
            del result[k]
            result.append(temp)
        else:
            k += 1
            result.append(lst[i])
    watch = sum(list(map(lambda x:x[1]-x[0], result)))
    return watch

def MovieTimesAct2(lst):
    s = set()
    for w in lst:
        s = s.union(range(*w))
    print(len(s))

if __name__ == "__main__":
    lst = [(0, 10), (15, 25), (12, 20), (30, 48)]
    print(MovieTimes(lst))
    print(MovieTimesAct2(lst))
