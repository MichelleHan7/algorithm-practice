class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        path = []
        n = len(candidates)
        def dfs(i, left):
            if left == 0:
                ans.append(path.copy())
                return 
            if i == n:
                return
            if candidates[i] <= left:
                path.append(candidates[i])
                dfs(i, left - candidates[i])
                path.pop()
            dfs(i+1, left)
        dfs(0, target)
        return ans