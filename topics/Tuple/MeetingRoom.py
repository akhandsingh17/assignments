"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1

"""


class Solution:
    def minMeetingRooms(self, intervals) -> int:

        if not intervals:
            return 0

        cnt = 1
        intervals = sorted(intervals, key=lambda x: x[1])  # sort the input interval based on meeting start time
        for i in range(1, len(intervals)):
            if intervals[i-1][1] <= intervals[i][0]:
                continue
            else:
                cnt += 1
        return cnt

if __name__ == "__main__":
    s = Solution()
    assert s.minMeetingRooms(intervals=[[0, 30], [15, 20], [5, 10]]) == 2
    assert s.minMeetingRooms(intervals=[[7, 10], [2, 4]]) == 1
    assert s.minMeetingRooms(intervals=[]) == 0
    assert s.minMeetingRooms(intervals=[[5, 8], [6,8]]) == 2
    assert s.minMeetingRooms(intervals=[[9,10],[4,9],[4,17]]) == 2
    assert s.minMeetingRooms(intervals=[[1,5],[8,9],[8,9]]) == 2
