# 根据我上面的代码改出来的
# 保持的原则：重复元素可以一起被选，但不能在同一层被当成不同选择。
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []
        n = len(candidates)
        def dfs(i, left):
            if left == 0:
                ans.append(path.copy())
                return
            if left < 0 or i == n:
                return 
            # 选
            # 选择的时候不跳哦！不是说不能选择重复的数字
            path.append(candidates[i])
            dfs(i+1, left-candidates[i])
            path.pop()
            # 不选
            # 这里要跳是因为如果不选一个数，下一个数还是一样的数字的话，相当于再check一遍，那肯定是不能选择的
            i += 1
            while i < n and candidates[i] == candidates[i-1]:
                i += 1
            dfs(i, left)
            
        dfs(0, target)
        return ans