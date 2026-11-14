class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        nodeMap = defaultdict(list)
        for u, v, w in times:
            nodeMap[u].append((v, w))
        
        minHeap = [(0, k)]
        visited = set()
        
        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return weight
            for nei, w in nodeMap[node]:
                heapq.heappush(minHeap, (weight + w, nei))
        
        return -1 if len(visited) != n else weight