class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indegree = [0] * numCourses
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[pre].append(crs)
            indegree[crs] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        finish = 0
        while q:
            crs = q.popleft()
            finish += 1
            for nei in preMap[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return finish == numCourses