class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        minheap = []
        for x, y in points:
            minheap.append([x*x + y*y, x, y])
        heapq.heapify(minheap)
        ans = []
        while k > 0:
            d = heapq.heappop(minheap)
            ans.append([d[1], d[2]])
            k -= 1
        return ans