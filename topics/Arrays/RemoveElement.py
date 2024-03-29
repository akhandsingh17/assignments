"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1)
extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.
"""


class Solution:
    def removeElement(self, nums, val: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1
        return right


if __name__ == "__main__":
    s = Solution()
    assert (s.removeElement(nums=[3, 2, 2, 3], val=3)) == 2
    assert (s.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2)) == 5
