
def UnionIntersection(lst1, lst2):
    return set(lst1).union(set(lst2))



def SubsetArray(ary1,ary2):
    return set(ary1).intersection(set(ary2))


def main():

    lst1 = [1, 3, 4,3, 5, 7,5]
    lst2 = [2, 3, 5, 6,5]
    print UnionIntersection(lst1,lst2)

    ary1 = [11, 1, 13, 21, 3, 7,1]
    ary2 = [11,3, 7,1,1]
    print SubsetArray(ary1, ary2)


if __name__=='__main__':
    main()


