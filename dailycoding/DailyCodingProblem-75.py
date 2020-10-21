'''
This problem was asked by Microsoft.
Given an array of numbers, find the length of the longest increasing subsequence in the
array. The subsequence does not necessarily have to be contiguous.
For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest
increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
'''

def DailyCodingProblem75(ary):

    sub=[1]*len(ary)

    for i in range(1,len(ary)):
        for j in range(0,i):
            if ary[j]<ary[i]:
                tmp=sub[j]+1
                if tmp>sub[i]:
                    sub[i]=tmp

    return sorted(sub,reverse=True)[0]

def main():

    ary=[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print(DailyCodingProblem75(ary))

if __name__=='__main__':
    main()