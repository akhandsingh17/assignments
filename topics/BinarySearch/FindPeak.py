"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
"""

class Solution:
    def findPeakElement(self, nums):
        low, high = 0, len(nums)
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > max(nums[mid - 1], nums[mid + 1]):
                return mid
            elif nums[mid - 1] < nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1

if __name__ == "__main__":
    s = Solution()
    print(s.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
