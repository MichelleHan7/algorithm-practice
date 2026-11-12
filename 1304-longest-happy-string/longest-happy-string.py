class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        minHeap = []
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count < 0:
                minHeap.append((count, char))
        heapq.heapify(minHeap)
        ans = ''
        while minHeap:
            count, char = heapq.heappop(minHeap)
            if len(ans) >= 2 and ans[-1] == ans[-2] == char:
                if not minHeap:
                    break
                count1, char1 = heapq.heappop(minHeap)
                ans += char1
                if count1 + 1 < 0:
                    heapq.heappush(minHeap, (count1+1, char1))
                heapq.heappush(minHeap, (count, char))
            else:
                ans += char
                if count + 1 < 0:
                    heapq.heappush(minHeap, (count+1, char))
        return ans