def myAtoi(s):

    if len(s) < 1:
        return 0

    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    sign, base, i = 1, 0, 0

    while s[i] == ' ' and i < len(s) - 1: ## Do this second conditional, or it will fail NEARLY every case.
        i += 1

    if s[i].isalpha():  # See if you can do this WITHOUT using an internal method
        return 0

    if s[i] == '-' or s[i] == "+": # Seems silly, but you might hit multiple signs. If that happens, uh-oh.
        if s[i] == '-':
            sign = -1
        i += 1

    while i < len(s) and s[i] >= '0' and s[i] <= '9':            # At this point, we only really care about the first set of numbers.
        base = 10 * base + (ord(s[i]) - ord('0'))
        i += 1


    val = base * sign

    ## We can refine this by just taking the val, checking the sign and checking the max for the negative, minumum for the positive if that makes sense.
    if val > INT_MAX:   # so, instead, if sign == 1 then return min(val, int_max)
        return INT_MAX
    elif val < INT_MIN: #  elsewise, return the negative of max(val, int_mix)
        return INT_MIN
    else:
        return val

if __name__ == "__main__":
    print(myAtoi(s = "42"))
    print(myAtoi(s = "   -42"))
    print(myAtoi(s = "4193 with words"))
    print(myAtoi(s = "words and 987"))