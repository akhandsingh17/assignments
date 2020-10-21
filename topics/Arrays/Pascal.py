"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""

class Solution:
    def generate(self, numRows):
        result = []
        if not numRows:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        if numRows >= 3:
            last = self.generate(numRows-1)
            result.extend(last)
            prev = last[-1][0]
            curr = 0
            temp = [prev]
            for i in range(1, len(last[-1])):
                curr = last[-1][i]
                total = prev + curr
                temp.append(total)
                prev = curr
            temp.append(prev)
            result.append(temp)
            return result

if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))

