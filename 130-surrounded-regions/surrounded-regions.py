class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        stay = set()

        def dfs(r, c, notChange):
            if  r < 0 or r >= m or c < 0 or c >= n or board[r][c] == 'X' or (r, c) in notChange:
                return 
            notChange.add((r, c))
            dfs(r + 1, c, notChange)
            dfs(r - 1, c, notChange)
            dfs(r, c + 1, notChange)
            dfs(r, c - 1, notChange)

        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0, stay)
            if board[i][n-1] == 'O':
                dfs(i, n-1, stay)
        
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j, stay)
            if board[m-1][j] == 'O':
                dfs(m-1, j, stay)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in stay:
                    board[i][j] = 'X'