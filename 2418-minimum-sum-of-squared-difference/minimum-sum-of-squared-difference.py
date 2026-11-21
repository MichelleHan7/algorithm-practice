class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left = 0
        right = max(diff)
        while left <= right:
            mid = (left + right) // 2
            ops = sum([max(0, d-mid) for d in diff])
            if ops <= k:
                right = mid - 1
            else:
                left = mid + 1
        ans = 0
        for d in diff:
            if d > left:
                ans += left ** 2
                k -= d-left
            else:
                ans += d**2
            
        return ans - k * (2 * left - 1)