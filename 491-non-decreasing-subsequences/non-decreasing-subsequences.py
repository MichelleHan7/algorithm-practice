class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        ans = set()
        path = []
        n = len(nums)

        def dfs(i, prev):
            if i == n:
                if len(path) >= 2:
                    ans.add(tuple(path))
                return
            # not choose nums[i]:
            dfs(i+1, prev)
            if nums[i] >= prev:
                # choode nums[i]
                path.append(nums[i])
                dfs(i+1, nums[i])
                path.pop()
        
        dfs(0, float('-inf'))
        return list(ans)