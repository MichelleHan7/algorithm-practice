class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        path = []
        n = len(s)
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            
            for j in range(i, n):
                string = s[i:j+1]
                if string == string[::-1]:
                    path.append(string)
                    dfs(j+1)
                    path.pop()

        dfs(0)
        return ans
        