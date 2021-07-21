"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and
return its sum.
Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""

from sys import maxsize

class Solution:
    def maxSubArray(self, nums) -> int:
        max_so_far = -maxsize - 1
        max_ending_here = 0

        for i in range(0, len(nums)):
            max_ending_here += nums[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here

            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far

if __name__ == "__main__":
    s = Solution()
    assert (s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])) == 6
    assert (s.maxSubArray([1])) == 1
    assert (s.maxSubArray([0])) == 0
    assert (s.maxSubArray([-1])) == -1
    assert (s.maxSubArray([-2147483647])) == -2147483647


