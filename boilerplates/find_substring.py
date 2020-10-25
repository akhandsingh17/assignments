def find_substring(substr, str_exp):
    """
    Find the number of substrings in a given string expression. Time complexity (M*N)
    :param str_exp:
    :return:
    """
    k = len(substr)  # length of the substring
    cnt = 0
    for i in range(len(str_exp)):
        if str_exp[i:i+k] == substr:
            cnt += 1
    return cnt

if __name__ == "__main__":
    print(find_substring('mem', "The cat says memem, meome for melog"))
