class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones) # max heap
        while len(stones) >= 2:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            if s1 == s2:
                continue
            else:
                heapq.heappush(stones, s1-s2)
        return abs(stones[0]) if stones else 0

