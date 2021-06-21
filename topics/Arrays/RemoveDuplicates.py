"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new
length.Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1)
extra memory.

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 2, nums = [0,1,2,3,4]
Explanation: Your function should return length = 2

"""

class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 0:
            return 0

        k = 0
        for i in range(1, len(nums)):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]
        return k+1

if __name__ == "__main__":
    s = Solution()
    assert (s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])) == 5