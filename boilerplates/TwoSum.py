"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

class Solution:
    def twoSum(self, nums, target: int):
        dct = {}
        for idx, num in enumerate(nums):
            comp = target - num
            if comp in dct.keys():
                return [dct[comp], idx]
            else:
                dct[num] = idx

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum(nums=[2, 7, 11, 15], target=9))
    print(s.twoSum(nums=[-1, 0, 1, 2, -1, -4], target=3))