class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        pre = [0] * n
        pre[0] = height[0]
        for i in range(1, n):
            pre[i] = max(pre[i-1], height[i])
        suf = [0] * n
        suf[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            suf[i] = max(height[i], suf[i+1])
        ans = 0
        for i in range(n):
            ans += min(suf[i], pre[i]) - height[i]
        return ans