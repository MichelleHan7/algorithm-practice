class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest = 0
        left = right = 0
        length = 0
        while right < len(nums):
            right += 1
            length += 1
            while right < len(nums) and nums[right] > nums[right - 1]:
                length += 1
                right += 1
            longest = max(longest, right - left)
            left = right
        left = right = 0
        length = 0
        while right < len(nums):
            right += 1
            length += 1
            while right < len(nums) and nums[right] < nums[right - 1]:
                length += 1
                right += 1
            longest = max(longest, right - left)
            left = right
        return longest
        
