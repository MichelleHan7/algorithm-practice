class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        maxDp = [1] * n
        minDp = [1] * n
        maxDp[0] = minDp[0] = nums[0]

        for i in range(1, n):
            minDp[i] = min(minDp[i-1] * nums[i], maxDp[i-1] * nums[i], nums[i])
            maxDp[i] = max(maxDp[i-1] * nums[i], minDp[i-1] * nums[i], nums[i])
        
        return max(maxDp)