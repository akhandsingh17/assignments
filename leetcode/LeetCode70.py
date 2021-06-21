"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

1 <= n <= 45

with  Brute force   Time complexity : O(2n).
with Recursion with Memoization Time complexity : O(n)
"""

class Solution:
    cache = {}
    def climbStairs(self, n):
        if n < 3:
            return n
        else:
            return self._climbStairs(n-1) + self._climbStairs(n-2)

    def _climbStairs(self, n):
        if n not in self.cache.keys():
            self.cache[n] = self.climbStairs(n)
        return self.cache[n]

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(3))
