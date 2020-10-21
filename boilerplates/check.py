
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
    total_time = 0

    if len(lst) == 0 : return total_time

    lst.sort(key= lambda x : x[0])
    print(lst)
    res=[]
    for i in range(len(lst)) :
        if i == 0: res.append(lst[0])

        if res[-1][1] >= lst[i][0]:
            res[-1][1] = max(res[-1][1], lst[i][1])

        if res[-1][1] < lst[i][0]:
            res.append(lst[i])

    for i in range( len(res)):
        total_time = total_time + (res[1]-res[0])
    return total_time

if __name__ == "__main__":
    lst = [(0, 10), (15, 25), (12, 20), (30, 48)]
    print(MovieTimes(lst))
