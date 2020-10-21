"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

class Solution:
    def twoSum(self, nums, target: int):
        dct = {value: idx for idx, value in enumerate(nums)}
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in dct:
                if dct[pair] != i:
                    return [i, dct[pair]]
        return []

def main():
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))

if __name__=='__main__':
    main()