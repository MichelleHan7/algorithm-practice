class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])

        # return the area of current island
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            d = dfs(i+1, j)
            u = dfs(i-1, j)
            r = dfs(i, j+1)
            l = dfs(i, j-1)
            return 1 + d + u + l + r

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    ans = max(area, ans)
        return ans