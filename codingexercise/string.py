def SingleOccurence(ary):
    dct={}
    for i in (ary):
        if i not in dct:
            dct[i]=1
        else:
            count = dct[i]+1
            dct[i] = count
    return list(filter(lambda x: x[1]==1 ,dct.items()))

def main():
    ary = [1, 2, 2, 2, 3, 4, 56, 3, 3, 3, 7, 9, 4, 9, 4, 85, 6, 34, 6, 1, 10, 34, 45]
    print(SingleOccurence(ary))

if __name__=='__main__':
    main()

