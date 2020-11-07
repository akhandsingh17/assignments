"""
In a given integer array nums, there is always exactly one largest element.
Find whether the largest element in the array is at least twice as much as every other number in the array.
If it is, return the index of the largest element, otherwise return -1.
"""

class Solution:
    def dominantIndex(self, nums) -> int:
        dominant = max(nums)
        flag = False
        for i in range(len(nums)):
            try:
                if nums.index(dominant) != i:
                    if dominant // nums[i] >= 2:
                        flag = True
                    else:
                        flag = False
                        break
            except ZeroDivisionError:
                flag = True
                continue

        if flag or len(nums) == 1:
            return nums.index(dominant)
        else:
            return -1

if __name__ == "__main__":
    nums = [0, 2, 0, 3]
    s = Solution()
    print(s.dominantIndex(nums))