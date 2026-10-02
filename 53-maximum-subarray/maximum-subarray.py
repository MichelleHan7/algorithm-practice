class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = -inf
        minSum = 0
        s = 0

        for num in nums:
            s += num
            maxSum = max(maxSum, s-minSum)
            minSum = min(minSum, s)
        return maxSum