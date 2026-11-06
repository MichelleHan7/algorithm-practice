class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()
        ans = []

        def dfs(i, j, visited, prevHeight):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited:
                return
            if heights[i][j] >= prevHeight:
                visited.add((i, j))
                dfs(i+1, j, visited, heights[i][j])
                dfs(i-1, j, visited, heights[i][j])
                dfs(i, j+1, visited, heights[i][j])
                dfs(i, j-1, visited, heights[i][j])
            

        for i in range(m):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, n-1, atl, heights[i][n-1])

        for j in range(n):
            dfs(0, j, pac, heights[0][j])
            dfs(m-1, j, atl, heights[m-1][j])

        for i in range(m):
            for j in range(n):
                if (i, j) in pac and (i, j) in atl:
                    ans.append((i, j))
        return ans