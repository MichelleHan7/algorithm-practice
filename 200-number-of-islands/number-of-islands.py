class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def bfs(i, j):
            q = deque([(i, j)])
            while q:
                grid[i][j] == '0'
                i, j = q.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= m or nj < 0 or nj >= n or grid[ni][nj] == '0':
                        continue
                    q.append((ni, nj))
                    grid[ni][nj] = '0'

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    bfs(i, j)
        return ans