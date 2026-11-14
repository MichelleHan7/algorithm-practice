class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for j in range(n):
                if j == node:
                    continue
                if isConnected[node][j] == 1:
                    dfs(j)

        ans = 0
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i not in visited:
                    ans += 1
                    dfs(i)
        return ans