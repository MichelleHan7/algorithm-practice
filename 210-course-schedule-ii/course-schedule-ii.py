class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        indegree = [0] * numCourses # 每个课
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            indegree[crs] += 1
            preMap[pre].append(crs) # map of number of courses that needs it to be finished
        q = deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
        ans = []
        finish = 0
        while q:
            node = q.popleft()
            ans.append(node)
            finish += 1
            for c in preMap[node]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
        if finish != numCourses:
            return []
        return ans
