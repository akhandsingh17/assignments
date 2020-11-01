def PlusOne(ary, n):
    val = n
    carry = 0
    final = []
    for i in range(len(ary)-1, -1, -1):
        val = val + ary[i] + carry
        final.append(str(val % 10))
        carry = int(val/10)
        val = 0
    if carry > 0:
        final.append(str(carry))
    return ''.join(reversed(final))


if __name__ == "__main__":
    print(PlusOne([9, 9, 9, 7], 9))