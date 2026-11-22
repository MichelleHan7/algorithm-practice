class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        n = len(nums)
        down = up = 1

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                up = down + 1
            if nums[i] < nums[i-1]:
                down = up + 1
        
        return max(up, down)