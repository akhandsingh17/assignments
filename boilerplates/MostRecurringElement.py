
def MostRecurringElement(tup):
    """
    Find out the most recurring element from a given tuple
    :param tup:
    :return:
    """
    dct = {}
    for key in tup:
        if key in dct.keys():
            dct[key] = 1 + dct.get(key, 0)
        else:
            dct[key] = 1
    return sorted(dct.items(), key=lambda x: x[1])[-1][0]

if __name__ == "__main__":
    tup = (4, 8, 4, 7, 8, 8, 5, 2, 7, 7, 7, 7, 3, 2, 1, 1)
    print(MostRecurringElement(tup))