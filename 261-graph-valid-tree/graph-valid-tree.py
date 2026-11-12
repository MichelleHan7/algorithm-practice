class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        nodeMap = defaultdict(list)
        for u, v in edges:
            nodeMap[u].append(v)
            nodeMap[v].append(u)
        
        visited = set()

        def dfs(node, par):
            if node in visited:
                return False
            visited.add(node)
            for nei in nodeMap[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
