def ReverseNumber(num):

    # Constants.
    MAX_INT = 2147483647 # 2**31 - 1
    MIN_INT = -2147483648       # -2**31

    if num == 0 :
        return num

    neg_flag = True if num < 0 else False
    num = abs(num)
    found = False
    result = []
    while num != 0:
        key = num % 10  # get the reminder by division base 10
        if key == 0 and not found:
            num = int(num/10)
            continue
        else:
            found = True
            result.append(str(key))
        num = int(num/10)
    output = int(''.join(result))
    if output > MAX_INT or output < MIN_INT:
        return 0
    return output if not neg_flag else (-1) * output

if __name__ == "__main__":
    assert (ReverseNumber(340500)) == 5043
    assert (ReverseNumber(-123)) == -321
    assert (ReverseNumber(0)) == 0
    assert (ReverseNumber(1534236469)) == 0
