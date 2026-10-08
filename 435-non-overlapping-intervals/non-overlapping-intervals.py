class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        ans = 0
        end = -inf
        
        for i, inter in enumerate(intervals):
            if inter[0] >= end:
                end = max(end, inter[1])
            else:
                end = min(inter[1], end)
                ans += 1
        
        return ans