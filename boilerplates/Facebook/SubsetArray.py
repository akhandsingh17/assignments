def SubsetArray(ary1, ary2):
    """
    check if array 1 is subset of array 2 or vice-versa. A subset array means that all the elements from one array
    are present in the other array
    :param ary1:
    :param ary2:
    :return:
    """
    if len(ary1) > len(ary2):
        big = ary1
        small = ary2
    else:
        big = ary2
        small = ary1
    dct = {}
    for key in big:
        dct[key] = 1 + dct.get(key, 0)

    for key in small:
        if key in dct.keys() and dct.get(key) > 0:
            dct[key] = dct.get(key) - 1
        else:
            return False
    return True

if __name__ == "__main__":
    ary1 = [11, 1, 13, 21, 3, 7, 1]
    ary2 = [11, 3, 7, 1, 1]
    assert (SubsetArray(ary1, ary2)) == True
