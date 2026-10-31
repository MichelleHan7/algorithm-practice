class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # bucket sort
        cnt = Counter(nums)
        max_cnt = max(cnt.values())
        buckets = [[] for _ in range(max_cnt+1)]

        for num, c in cnt.items():
            buckets[c].append(num)
        
        ans = []  
        for i, e in enumerate(reversed(buckets)):
            ans += e
            if len(ans) == k:
                return ans