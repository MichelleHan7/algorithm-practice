class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        ans = []

        for i, [start, end] in enumerate(intervals):
            if newInterval[1] < start:
                ans.append(newInterval)
                return ans + intervals[i:]
            elif end < newInterval[0]:
                ans.append([start, end])
            else:
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]
        
        ans.append(newInterval)

        return ans
