class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        odd = float('-inf')
        even = 0

        for num in nums:
            odd = max(odd, even + num)
            even = max(even, odd - num)
        
        return max(odd, even)