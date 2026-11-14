class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        m, n = len(board), len(board[0])

        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or board[i][j] != 'X':
                return 
            visited.add((i, j))
            for di, dj in directions:
                dfs(i+di, j+dj)

        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i, j) not in visited:
                    dfs(i, j)
                    count += 1
        return count