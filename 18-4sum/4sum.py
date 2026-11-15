class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n-3):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue
                k = j + 1
                l = n - 1
                while k < l:
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        while k < l and nums[k-1] == nums[k]:
                            k += 1
                        l -= 1
                        while k < l and nums[l+1] == nums[l]:
                            l -= 1
                    elif s > target:
                        l -= 1
                    else:
                        k += 1
        return ans