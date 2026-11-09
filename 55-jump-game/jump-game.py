class Solution:
    def canJump(self, nums: list[int]) -> bool:
        far = nums[0]
        for i, num in enumerate(nums):
            if far < i:
                return False
            far = max(far, i + num)
        return True