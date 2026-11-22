class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        ans = []
        path = []
        n = len(s)

        def dfs(i):
            if i == n:
                if len(path) == 4:
                    ans.append('.'.join(path))
                return 
            
            for j in range(i, min(i+3, n)):
                seg = s[i:j+1]
                if 0 <= int(s[i:j+1]) <= 255:
                    if len(s[i:j+1]) > 1 and s[i:j+1][0] == '0':
                        break
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return ans