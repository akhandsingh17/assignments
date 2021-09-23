"""Given an array nums which consists of non-negative integers and an integer m, you can split the array into m
non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.



Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.


"""

from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def isok(mid):
            split = 1
            cursum = 0
            for num in nums:
                if cursum + num > mid:
                    split += 1
                    cursum = 0
                cursum += num
            return split <= m

        left = max(nums)
        right = sum(nums) + 1
        while left < right:
            mid = left + (right - left) // 2
            if isok(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    s = Solution()
    print(s.splitArray(nums=[7, 2, 5, 10, 8], m=2))
