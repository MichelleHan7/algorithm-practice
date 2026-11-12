class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # adjacency list
        nodeMap = defaultdict(list)
        for u, v, w in edges:
            nodeMap[u].append((v, w))
        
        dist = [[float('inf')] * (k+1) for _ in range(n)]
        dist[0][1] = 0
        
        minHeap = [(0, 0, 1)] # total weight, node, the number of consecutive identical characters at the END of the current path
        heapq.heapify(minHeap)
        while minHeap:
            w, node, count = heapq.heappop(minHeap)
            if w > dist[node][count]: # prune more expensive paths
                continue
            if node == n-1: # return the correct answer
                return w
            cur_label = labels[node]
            for n1, w1 in nodeMap[node]:
                if labels[n1] == cur_label:
                    new_count = count + 1
                else:
                    new_count = 1 
                
                if new_count > k:
                    continue
                new_weight = w + w1
                if new_weight >= dist[n1][new_count]:
                    continue
                dist[n1][new_count] = new_weight
                heapq.heappush(minHeap, (new_weight, n1, new_count))
        return -1