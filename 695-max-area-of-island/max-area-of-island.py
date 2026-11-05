class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            area = 1
            grid[i][j] = 0
            area += dfs(i+1, j)
            area += dfs(i-1, j)
            area += dfs(i, j+1)
            area += dfs(i, j-1)
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        return ans