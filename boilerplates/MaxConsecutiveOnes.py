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
        count = 0
        current_max = 0
        for i in nums:
            if i == 1:
                count += 1
                current_max = max(count, current_max)
                continue
            else:
                count = 0
        return current_max

if __name__ == "__main__":
        s = Solution()
        print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
        print(s.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))