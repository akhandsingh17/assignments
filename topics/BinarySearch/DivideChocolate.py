"""
You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your k friends so you start cutting the chocolate bar into k + 1 pieces using k
cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

"""
from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def isFail(mid):
            count = 0
            cursum = 0
            for sweet in sweetness:
                cursum += sweet
                if cursum >= mid:
                    count += 1
                    cursum = 0
            return count < k + 1

        left = min(sweetness)
        right = sum(sweetness) + 1
        while left < right:
            mid = left + (right - left) // 2
            if isFail(mid):
                right = mid
            else:
                left = mid + 1
        return left - 1


if __name__ == '__main__':
    s = Solution()
    print(s.maximizeSweetness(sweetness=[1, 2, 3, 4, 5, 6, 7, 8, 9], k=5))
