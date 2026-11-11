class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        dp = {}
        
        for num in arr:
            dp[num] = dp.get(num-difference, 0) + 1
        
        return max(dp.values())