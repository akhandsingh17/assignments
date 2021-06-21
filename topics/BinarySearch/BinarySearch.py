"""
Given a sorted (in ascending order) integer array nums of n elements and a target value,
write a function to search target in nums. If target exists, then return its index, otherwise return -1.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

"""

class Solution:
    def search(self, nums, target: int) -> int:
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
        return -1

if __name__ == "__main__":
    s = Solution()
    assert s.search([-1,0,3,5,9,12], 9) == 4
    assert (s.search([5], 5)) == 0
