def uniqueNumber(num):
    """
    check if the given integer number if comprised of unique digits
    :param num:
    :return: Ture or Flase
    """
    dct = {}
    key = 0
    while num != 0:
        key = num % 10
        if key in dct.keys():
            return False
        else:
            dct[key] = 1
        num = int(num/10)
    return True

if __name__ == "__main__":
    num = 123
    assert(uniqueNumber(num)) == True
    
