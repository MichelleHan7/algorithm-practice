class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefix_map = {0: -1}
        total = 0

        for i, num in enumerate(nums):
            total += num
            mod = total % k

            if mod in prefix_map:
                if i - prefix_map[mod] >= 2:
                    return True
            else:
                prefix_map[mod] = i

        return False