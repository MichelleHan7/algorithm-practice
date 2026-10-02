class Solution:
    def canJump(self, nums: list[int]) -> bool:
        canJump = 0
        for i, num in enumerate(nums):
            if i > canJump:
                return False
            canJump = max(canJump, i + num)
        return True
