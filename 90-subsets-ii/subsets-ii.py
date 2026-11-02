class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        path = []
        ans = []
        n = len(nums)
        nums.sort()

        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            # choose
            path.append(nums[i])
            dfs(i+1)
            path.pop()
            # not choose
            i += 1
            while i < n and nums[i] == nums[i-1]:
                i += 1
            dfs(i)
        dfs(0)
        return ans