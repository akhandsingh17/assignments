"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all
meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true

"""

class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        intervals = sorted(intervals, key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i-1][1] <= intervals[i][0]:
                continue
            else:
                return False
        return True


if __name__=='__main__':
    s = Solution()
    print(s.canAttendMeetings(intervals=[[0, 30], [5, 10], [15, 20]]))
    print(s.canAttendMeetings(intervals=[[7, 10], [2, 4]]))
    print(s.canAttendMeetings(intervals=[[13, 15], [1, 13]]))