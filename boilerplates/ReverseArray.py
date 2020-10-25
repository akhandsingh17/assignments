def ReverseAry(ary):
    """
    Reverse the input array in constant time
    :param ary:
    :return:
    """
    result = []
    key = len(ary) -1
    while key >= 0:
        result.append(ary[key])
        key -= 1
    return result

if __name__ == "__main__":
    ary = [1, 2, 3, 4, 5, 6, 7]
    print(ReverseAry(ary))