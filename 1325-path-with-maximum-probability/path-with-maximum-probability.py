class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        nodeMap = defaultdict(list)
        for i, [a, b] in enumerate(edges):
            nodeMap[a].append((b, succProb[i]))
            nodeMap[b].append((a, succProb[i]))

        minHeap = [(-1.0, start_node)]
        visited = set()

        while minHeap:
            prob, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            if node == end_node:
                return -prob
            for nei, neiProb in nodeMap[node]:
                
                heapq.heappush(minHeap, (neiProb * prob, nei))
        
        return 0.0
