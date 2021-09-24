"""

A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.



Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

refer - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/discuss/819184/6-questions-in-one-template-of-binary-search-for-beginners-python

Method:

left - inclusive; right - exclusive
use while left < right
if finding min value, define 'isok' function (and return left) ;
if finding max value, define 'isfail' function (and return left-1).


"""

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isOk(mid):
            day = 1
            cursum = 0
            for weight in weights:
                if cursum + weight > mid:
                    day += 1
                    cursum = 0
                cursum += weight
            return day <= days

        left = max(weights)
        right = sum(weights) + 1
        while left < right:
            mid = left + (right - left) // 2
            if isOk(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    s = Solution()
    print(s.shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5))