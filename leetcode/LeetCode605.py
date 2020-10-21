'''
605. Can Place Flowers

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
'''

import collections

def LeetCode605(ary,n):

    flg=False
    for i in range(1,len(ary)-1):
        if ary[i]==0:
            if ary[i-1]==1 or ary[i+1]==1:
                continue
            else:
                n=n-1
        if n==0:
            flg=True
            break
    return flg

def main():

    ary=[1,0,0,0,1]
    n=1
    print(LeetCode605(ary,n))

    ary = [1, 0, 0, 0, 1]
    n = 2
    print(LeetCode605(ary, n))

if __name__=='__main__':
    main()