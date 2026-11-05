class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q = deque()
        fresh = 0
        m, n = len(grid), len(grid[0])
        time = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while q and fresh:
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        q.append((ni, nj))
            time += 1
        return -1 if fresh else time

