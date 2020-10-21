def findNumbers(li, diff):
    # find paris which have a difference of 3
    dic = {}
    res = []
    for i in li:
        if i not in dic:
            dic[i+diff] = [i]
            dic[i-diff] = [i]
        else:
            res.extend(map(lambda x:(x,i),dic[i]))
            if i+diff not in dic:
                dic[i+diff]=[i]
            if i-diff not in dic:
                dic[i-diff]=[i]
    return res


def main():
    # Driver program
    arr = [1, 5, 3, 4, 2, 9, 6]
    diff = 3
    dct=findNumbers(arr, diff)
    print dct

if __name__=='__main__':
    main()


