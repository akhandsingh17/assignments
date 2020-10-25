def ReplaceString(str_exp):
    """
    replace the input string with specified delimiter. The delimiter can be present anywhere in the input string.
    :param str_exp:
    :return:
    """
    result = ''
    lst = [word for word in str_exp.split('$')]
    found = False
    for word in lst:
        if word == '' and not found:
            found = True
            continue
        elif word != '' and not found:
            result = result + word + ' '
        elif word == '' and found:
            continue
        else:
            result = result + word + ' '
    return  result

if __name__ == "__main__":
    str1 = '$$$$$Mr$$John$Smith$$$$$$'
    str2 = 'Mr$$John$Smith'
    str3 = '$$$$$Mr$$John$Smith'
    str4 = '$$$$$Mr$$John$$$$Smith$'
    print(ReplaceString(str1))
    print(ReplaceString(str2))
    print(ReplaceString(str3))
    print(ReplaceString(str4))