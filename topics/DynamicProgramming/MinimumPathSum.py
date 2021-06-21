"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which
minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""

class Solution:
    def minPathSum(self, grid) -> int:
        result = []
        if not grid:
            return grid
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = grid[0][i] + dp[0][i-1]
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1] + grid[i][j])
        return dp[m-1][n-1]

if __name__ == "__main__":
    s = Solution()
    m = [[1,3,1],[1,5,1],[4,2,1]]
    print(s.minPathSum(m))