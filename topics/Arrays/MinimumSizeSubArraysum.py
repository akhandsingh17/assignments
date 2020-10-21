"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous
subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

"""

import sys

class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        left, total = 0, 0
        ans = sys.maxsize
        for i in range(len(nums)):
            total += nums[i]
            while total >= s:
                ans = min(ans, i + 1 - left)
                total -= nums[left]
                left += 1
        return ans if ans != sys.maxsize else 0

if __name__ == "__main__":
    s = Solution()
    print(s.minSubArrayLen(s=7, nums=[2, 3, 1, 2, 4, 3]))