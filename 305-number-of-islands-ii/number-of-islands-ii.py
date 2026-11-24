class Solution:
    def numIslands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        ans = [0] * len(positions)
        par = {}
        degree = {}
        count = 0

        def find(node):
            while node != par[node]:
                par[node] = par[par[node]]
                node = par[node]
            return node

        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            if p1 == p2:
                return False
            if degree[p1] < degree[p2]:
                par[p1] = p2
                degree[p2] += degree[p1]
            else:
                par[p2] = p1
                degree[p1] += degree[p2]
            return True

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i, [r, c] in enumerate(positions):
            node = (r, c)
            if node in par:
                ans[i] = count
                continue
            par[node] = node
            degree[node] = 1
            count += 1

            for dr, dc in directions:
                nei = (r+dr, c+dc)
                if nei in par:
                    if union(nei, node):
                        count -= 1
            
            ans[i] = count
        return ans