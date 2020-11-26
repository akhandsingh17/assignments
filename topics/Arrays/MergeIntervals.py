"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.


Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""

class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])
        result = []
        k = 0
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            if result[k][1] >= intervals[i][0] and result[k][1] < intervals[i][1]:
                temp = [result[k][0], intervals[i][1]]
                del result[k]
                result.append(temp)
            elif result[k][1] < min(intervals[i][0], intervals[i][1]):
                k += 1
                result.append(intervals[i])
        return result


if __name__=='__main__':
    s = Solution()
    assert s.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert s.merge(intervals = [[1,4],[4,5]]) == [[1,5]]
    assert s.merge([[1,4],[2,3]]) == [[1,4]]