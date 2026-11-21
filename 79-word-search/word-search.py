class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            if k == len(word):
                return True
            if i >= m or i < 0 or j >= n or j < 0 or board[i][j] != word[k]:
                return
            board[i][j] = ''
            found = (
                dfs(i+1, j, k+1) or 
                dfs(i-1, j, k+1) or
                dfs(i, j+1, k+1) or
                dfs(i, j-1, k+1)
            )
            board[i][j] = word[k]
            return found 
        

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False