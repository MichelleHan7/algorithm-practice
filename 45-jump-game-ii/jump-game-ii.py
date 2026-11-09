class Solution:
    def jump(self, nums: list[int]) -> int:
        count = 0
        farest = 0
        curfar = 0

        for i in range(len(nums) - 1):
            farest = max(farest, i + nums[i])
            if i == curfar:
                curfar = farest
                count += 1
        
        return count