# Find closest number in array
# Given an array of sorted integers.
# We need to find the closest value to the given number.
# Array may contain duplicate values and negative numbers.


def ClosestNumberArray(ary, k):
    start, end = 0, len(ary) - 1

    if k > ary[-1]:
        return ary[-1]

    if k < ary[0]:
        return ary[0]

    while start + 1 < end:
        mid = (start + end) // 2
        if ary[mid] >= k:
            end = mid
        else:
            start = mid

    index = end
    if ary[start] >= k:
        index = start
    return index if (ary[index] - k) < (k - ary[index - 1]) else index - 1


def main():
    ary = [1, 2, 4, 5, 6, 6, 8, 9]
    k = 11
    print(ClosestNumberArray(ary, k))

    ary = [2, 5, 6, 7, 8, 8, 9]
    k = 4
    print(ClosestNumberArray(ary, k))


if __name__ == '__main__':
    main()
