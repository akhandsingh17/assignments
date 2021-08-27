"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Input: nums = []
Output: []

subarray sum equal to 0

"""
from typing import List, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int, current_index: int):
        dct = {}
        for idx, num in enumerate(nums):
            if idx != current_index:
                comp = target - num
                if comp in dct.keys():
                    return [nums[dct[comp]], nums[idx]]
                else:
                    dct[num] = idx

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for idx, target in enumerate(nums):
            temp = self.twoSum(nums, target, idx)
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
