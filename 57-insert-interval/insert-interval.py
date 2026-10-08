class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        ans = []

        for i, inter in enumerate(intervals):
            if newInterval[1] < inter[0]:
                ans.append(newInterval)
                ans += intervals[i:]
                return ans
            elif newInterval[0] > inter[1]:
                ans.append(inter)
            else:
                newInterval = [min(newInterval[0], inter[0]), max(newInterval[1], inter[1])]
        ans.append(newInterval)
        
        return ans