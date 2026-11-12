class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        ans = 0
        for n in nums:
            ans += abs(median - n)
        return ans
        