class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort()
        end = 0
        for s, e in intervals:
            if s >= end:
                end = e
            else:
                return False
        return True