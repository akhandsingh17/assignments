"""
Given a binary array, find the maximum number of consecutive 1s in this array.
Example 1:

Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.

"""

class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        cnt = 0
        current_max = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
                current_max = max(current_max, cnt)
            else:
                cnt = 0
        return current_max

if __name__ == "__main__":
    s = Solution()
    assert (s.findMaxConsecutiveOnes(nums=[1, 1, 0, 1, 1, 1])) == 3