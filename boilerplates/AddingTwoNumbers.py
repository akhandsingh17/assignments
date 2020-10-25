def AddingTwoNumbers(num1, num2):
    """
    Add two integer numbers without mathematical sum operator
    :param num1:
    :param num2:
    :return:
    """
    big = num1 if num1 > num2 else num2
    small = num1 if num1 < num2 else num2
    carry = 0
    result = []
    while big != 0:
        if small != 0:
            val = (big % 10) + (small % 10) + carry
            small = int(small/10)
        else:
            val = (big % 10) + carry
        carry = int(val/10)
        big = int(big/10)
        result.append(str(val % 10))
    if carry > 0:
        result.append(str(carry))
    return ''.join(reversed(result))

if __name__ == "__main__":
    num1 = 37
    num2 = 679
    print(AddingTwoNumbers(num1, num2))