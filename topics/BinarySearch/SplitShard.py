"""
How to partition an array of integers in a way that minimizes the maximum of the sum of each partition?

example:
[6, 4, 2, 11, 1, 1, 1, 10, 10]

Input:

A = {2, 1, 5, 1, 2, 2, 2}
K = 3

Expected output:

MaxSumBlock: 6
(with partition: {2, 1}, {5, 1}, {2, 2, 2})

In the expected output, the sums of each block are 3, 6 and 6. The max is 6.

Here is an non optimal partition:

partition: {2, 1}, {5}, {1, 2, 2, 2}

The sums of each block in that case are 3, 6 and 7. The max is hence 7. It is not a correct answer.

"""


class Solution:
    def minMaxSumBlock(self, nums, k):
        def isOk(mid):
            split = 1
            cursum = 0
            for num in nums:
                if cursum + num > mid:
                    split += 1
                    cursum = 0
                cursum += num
            return split <= k


        left = max(nums)
        right = sum(nums) + 1
        while left < right:
            mid = left + (right - left) // 2
            if isOk(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    s = Solution()
    assert s.minMaxSumBlock(nums=[2, 1, 5, 1, 2, 2, 2], k=3) == 6
    assert s.minMaxSumBlock(nums=[6, 4, 2, 11, 1, 1, 1, 10, 10], k=5) == 12

