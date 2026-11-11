class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted([num * num for num in nums])
        n = len(nums)
        minus = n // 2
        ans = 0
        for i in range(n):
            if i < minus:
                ans -= squares[i]
            else:
                ans += squares[i]
        return ans