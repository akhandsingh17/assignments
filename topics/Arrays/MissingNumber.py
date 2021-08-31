"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is
missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Input: nums = [3,0,1] Output: 2 Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,
3]. 2 is the missing number in the range since it does not appear in nums.

Input: nums = [0,1] Output: 2 Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,
2]. 2 is the missing number in the range since it does not appear in nums.

"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ap = n * (n + 1) // 2
        return ap - sum(nums)


if __name__ == "__main__":
    s = Solution()
    assert s.missingNumber([3, 0, 1]) == 2
    assert s.missingNumber([0, 1]) == 2
    assert s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
