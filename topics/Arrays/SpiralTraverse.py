class Solution(object):

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if not matrix:
            return result
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while (top <= bottom & left <= right):

            for i in range(left, right+1):
                result.append(matrix[top][i])

            for j in range(top + 1, bottom):
                result.append(matrix[j][right])

            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])

            for j in range(bottom - 1, top, -1):
                result.append(matrix[j][left])

            top += 1
            right -= 1
            left += 1
            bottom -= 1

        return result

if __name__ == "__main__":
    s = Solution()
    m = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]]
    #assert (s.spiralOrder(m)) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    m = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    #assert (s.spiralOrder(m)) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    m= []
    #assert s.spiralOrder(m) == []

    m = [[1, 2],
         [3, 4]]
    #assert (s.spiralOrder(m)) == [1, 2, 4, 3]

    m = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]
    print (s.spiralOrder(m))