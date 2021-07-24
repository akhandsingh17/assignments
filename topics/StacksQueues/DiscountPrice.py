"""
Given the array prices where prices[i] is the price of the ith item in a shop. There is a special discount for items in the shop,
if you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and
prices[j] <= prices[i], otherwise, you will not receive any discount at all

"""
from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i, num in enumerate(prices):
            while stack and prices[stack[-1]] >= num:
                popIndex = stack.pop()
                prices[popIndex] -= num
            stack.append(i)
        return prices


if __name__ == "__main__":
    prices = [8, 4, 6, 2, 3]
    s = Solution()
    assert s.finalPrices(prices) == [4, 2, 4, 2, 3]
