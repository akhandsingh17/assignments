"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(1, numRows+1):
            temp = []
            for j in range(1, i+1):
                temp.append(self.helper(i, j))
            result.append(temp)
        return result

    def helper(self, i, j):

        if j == 1 or j == i:
            return 1
        return self.helper(i-1, j-1) + self.helper(i-1, j)

if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))