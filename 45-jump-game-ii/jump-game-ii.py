class Solution:
    def jump(self, nums: list[int]) -> int:
        ans = 0
        cur_end = 0
        next_end = 0
        for i, num in enumerate(nums):
            next_end = max(next_end, i + num)
            if i == len(nums) - 1:
                return ans
            if i == cur_end:
                ans += 1
                cur_end = next_end
        
        return ans

