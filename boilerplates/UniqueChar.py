def UniqueChar(s):
    """
    check if the given input string is comprised of unique characters
    :param s: input string
    :return: True or False
    """

    dct = {}   # a dict with key as char and value as frequency
    for chr in s:
        if chr in dct.keys():
            return False
        else:
            dct[chr] = 1
    return True


if __name__ == "__main__":
    s = 'akhand'
    assert(UniqueChar(s)) == False