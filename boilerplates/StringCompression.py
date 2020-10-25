def StringCompression(str_exp):
    """
    compress the input string expression by encoding it. <char followed by frequency>
    :param str_exp:
    :return:
    """
    prev = str_exp[0]
    cnt = 1
    result = ''
    for i in range(1, len(str_exp)):
        if prev == str_exp[i]:
            cnt += 1
        else:
            result = result + prev + str(cnt)
            cnt = 1
        prev = str_exp[i]
    result = result + prev + str(cnt)
    return result

if __name__ == "__main__":
    str_exp = 'aabcccccaa'
    print(StringCompression(str_exp))