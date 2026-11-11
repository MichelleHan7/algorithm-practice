class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        prev_prefix = {}
        ans = float('-inf')

        for num in nums:
            if num-k in prev_prefix:
                ans = max(ans, prefix + num - prev_prefix[num-k])
            if num+k in prev_prefix:
                ans = max(ans, prefix + num - prev_prefix[num+k])
            if num not in prev_prefix:
                prev_prefix[num] = prefix
            else:
                prev_prefix[num] = min(prev_prefix[num], prefix)
            prefix += num
        return ans if ans != float('-inf') else 0
        