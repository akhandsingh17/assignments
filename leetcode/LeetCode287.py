'''
287. Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''

def LeetCode287(ary):

    for i in range(0,len(ary)):
        key=ary[i]

        if key in ary[:i] or key in ary[i+1:]:
            break
        else:
            key=-1
    return key

def main():

    ary=[1,3,4,2,2]
    print(LeetCode287(ary))

    ary = [3,1,3,4,2]
    print(LeetCode287(ary))


if __name__=='__main__':
    main()