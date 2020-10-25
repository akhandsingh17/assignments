def StringExpansion(str):
    """
    expand the input assuming that encoded string has a valid character followed by an integer value representing
    it's frequency
    :param str:
    :return:
    """
    result = []
    prev_char = ''
    for i in str:
        if ord(i) >= 48 and ord(i) <= 57:
            frequency = int(i)
            while frequency > 0:
                result.append(prev_char)
                frequency -= 1
        prev_char = i
    return ''.join(result)

if __name__ == "__main__":
    str_exp = 'a3b1c5a2d2'
    print(StringExpansion(str_exp))