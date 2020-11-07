"""
Given an array of integers nums, write a method that returns the "pivot" index of this array.
We define the pivot index as the index where the sum of the numbers to the left of the index is equal to
the sum of the numbers to the right of the index.
If no such index exists, we should return -1. If there are multiple pivot indexes,
you should return the left-most pivot index.

"""
class Solution:
    def pivotIndex(self, nums) -> int:
        totalsum = sum(nums[:])
        left_sum = 0
        for i in range(len(nums)):
            if(totalsum - nums[i] == left_sum):
                return i
            left_sum = left_sum + nums[i]
            totalsum = totalsum - nums[i]
        return -1

if __name__ == "__main__":
    nums = [1, 2, 1]
    s = Solution()
    print(s.pivotIndex(nums))