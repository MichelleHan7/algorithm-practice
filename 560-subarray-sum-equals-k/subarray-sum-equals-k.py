class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        presum = 0
        ans = 0
        for i, num in enumerate(nums):
            prefix[presum] += 1
            presum += num
            if presum - k in prefix:
                ans += prefix[presum - k]
        return ans