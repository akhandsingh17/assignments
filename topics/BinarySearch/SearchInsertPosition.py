"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

"""

class Solution:
    def searchInsert(self, nums, target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
        return low

if __name__ == "__main__":
    s = Solution()
    assert (s.searchInsert([1, 3, 5, 6], 5)) == 2
    assert (s.searchInsert([1, 3, 5, 6], 2)) == 1
    assert (s.searchInsert([1, 3, 5, 6], 7)) == 4
    assert (s.searchInsert([1, 3, 5, 6], 0)) == 0