class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        prefix = 0
        ans = []
        for num in nums:
            prefix += num
            ans.append(prefix)
        return ans