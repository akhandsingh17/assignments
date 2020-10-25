def ReverseNumber(num):
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
    return ''.join(result)


if __name__ == "__main__":
    n = 340500
    assert (ReverseNumber(n)) == '5043'