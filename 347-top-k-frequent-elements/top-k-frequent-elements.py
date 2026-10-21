class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        cnt = Counter(nums)
        maxCount = max(cnt.values())
        bucket = [[] for i in range(maxCount + 1)]

        for num, count in cnt.items():
            bucket[count].append(num)

        ans = []
        for i in range(len(bucket)-1, -1, -1):
            ans += bucket[i]
            if len(ans) == k:
                return ans
        
