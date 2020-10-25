def median(ary):
    ary = sorted(ary)
    if len(ary) % 2 == 0:
        mid = len(ary)/2
        result = (int(ary[mid]) + int(ary[mid+1])) / 2
    else:
        mid = int(len(ary)/2)
        result = ary[mid]
    return result

if __name__ == "__main__":
    ary1 = [5, 89, 20, 64, 20, 45]
    print(median(ary1))