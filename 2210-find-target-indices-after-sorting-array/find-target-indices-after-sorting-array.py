class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if left == n or left < 0 or nums[left] != target:
            return []
        ans = []
        right = left
        while right < n and nums[right] == nums[left]:
            ans.append(right)
            right += 1
        return ans
        