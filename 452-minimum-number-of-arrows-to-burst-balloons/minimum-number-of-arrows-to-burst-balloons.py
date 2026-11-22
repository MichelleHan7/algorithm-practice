class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        ans = 1
        end = points[0][1]
        i = 1
        for i in range(1, len(points)):
            if points[i][0] > end:
                ans += 1
                end = points[i][1]
            else:
                end = min(end, points[i][1])
        
        return ans