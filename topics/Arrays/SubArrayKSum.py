"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.


Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

"""


def AllSubArraySum(nums, k):
    result = []
    dict = {}
    dict.setdefault(0, []).append(-1)
    curr_sum = 0
    for idx, val in enumerate(nums):
        curr_sum += val
        if curr_sum -k in dict.keys():
            result.append(nums[(curr_sum-k): idx+1])
        elif val == k:
            result.append([val])
        else:
            dict.setdefault(curr_sum, []).append(idx)
    return len(result)

def main():
    print(AllSubArraySum(nums=[1, 2, 3], k=3))
    print(AllSubArraySum(nums=[1, 1, 1], k=2))

if __name__ == '__main__':
    main()
