class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                right = mid - 1
            else:
                left = mid + 1
        return nums[left]