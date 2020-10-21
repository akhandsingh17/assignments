"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.

"""

class Solution:
    def addDigits(self, num: int):
        total = 0
        if num <= 9:
            return num
        else:
            while num != 0:
                rem = num % 10
                total += rem
                num = int(num / 10)
        return self.addDigits(total)

if __name__ == "__main__":
    s = Solution()
    print(s.addDigits(38))
