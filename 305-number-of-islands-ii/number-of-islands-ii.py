class Solution:
    def numIslands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        parent = {}
        size = {}
        count = 0
        ans = []

        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        def union(a, b):
            p1, p2 = find(a), find(b)

            if p1 == p2:
                return False

            if size[p1] < size[p2]:
                p1, p2 = p2, p1

            parent[p2] = p1
            size[p1] += size[p2]

            return True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for r, c in positions:
            node = (r, c)

            if node in parent:
                ans.append(count)
                continue

            parent[node] = node
            size[node] = 1
            count += 1

            for dr, dc in directions:
                nei = (r + dr, c + dc)

                if nei in parent:
                    if union(node, nei):
                        count -= 1

            ans.append(count)

        return ans