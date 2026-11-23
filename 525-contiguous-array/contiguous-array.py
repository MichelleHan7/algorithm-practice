class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = 0
        longest = 0
        seen = {0: -1}

        for i, num in enumerate(nums):
            if num == 0:
                prefix -= 1
            else:
                prefix += 1
            
            if prefix in seen:
                longest = max(longest, i - seen[prefix])
            else:
                seen[prefix] = i
        
        return longest