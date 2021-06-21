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


class Solution:
    def maxSubArray(self, nums) -> int:
        best_sum = 0
        curr_sum = 0
        best_start = best_end = 0
        if len(nums) == 1:
            return nums[0]

        for curr_end, x in enumerate(nums):
            if curr_sum < 0:
                # Start a new sequence at the current element
                curr_start = curr_end
                curr_sum = x
            else:
                curr_sum += x
            if curr_sum > best_sum:
                best_sum = curr_sum
                best_start = curr_start
                best_end = curr_end + 1 # the +1 is to make 'best_end' exclusive
        return best_sum

if __name__ == "__main__":
    s = Solution()
    assert (s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])) == 6
    assert (s.maxSubArray([1])) == 1
    assert (s.maxSubArray([0])) == 0
    assert (s.maxSubArray([-1])) == -1
    assert (s.maxSubArray([-2147483647])) == -2147483647


