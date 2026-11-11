class Solution:
    def findStart(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = self.findStart(nums, target)
        end = self.findStart(nums, target + 1)
        if start >= len(nums) or start < 0 or nums[start] != target:
            return [-1, -1]
        return [start, end-1]