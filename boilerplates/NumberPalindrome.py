
def NumberPalindrome(num):
    """
    Given an integer number, check if the number is a palindrome.
    :param num:
    :return: True or False
    """
    reverse=[]
    orig = num
    while num != 0:
        key = num % 10
        num = int(num/10)
        reverse.append(str(key))
    if int(''.join(reverse)) == orig :
        return True
    else:
        return False


if __name__ == "__main__":
    num = 112211
    assert (NumberPalindrome(num)) == True
    num = 3344882
    assert (NumberPalindrome(num)) == False