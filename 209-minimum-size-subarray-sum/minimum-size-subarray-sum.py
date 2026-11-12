class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        prefix = 0
        left = 0
        ans = inf
        total = 0
        for right, num in enumerate(nums):
            total += num
            while total - prefix >= target:
                ans = min(ans, right - left + 1)
                prefix += nums[left]
                left += 1
        return ans if ans != inf else 0