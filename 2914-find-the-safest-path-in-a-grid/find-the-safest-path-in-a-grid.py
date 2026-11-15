class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    dist[i][j] = 0
        while q:
            ti, tj = q.popleft()
            for di, dj in directions:
                ni, nj = ti+di, tj+dj
                if 0 <= ni < n and 0 <= nj < n and dist[ni][nj] == -1:
                    dist[ni][nj] = dist[ti][tj] + 1
                    q.append((ni, nj))

    
        minHeap = [(-dist[0][0], (0, 0))]
        visited = set()
        while minHeap:
            f, (i, j) = heapq.heappop(minHeap)
            if (i, j) in visited:
                continue
            if (i, j) == (n-1, n-1):
                return -f
            visited.add((i, j))
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0 > ni or ni >= n or 0 > nj or nj >= n or (ni, nj) in visited:
                    continue
                new_f = max(f, -dist[ni][nj])
                heapq.heappush(minHeap, (new_f, (ni, nj)))
        return 0