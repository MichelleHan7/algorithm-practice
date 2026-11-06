class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        indegree = [0] * numCourses
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            indegree[crs] += 1
            preMap[pre].append(crs)
        
        q = deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)

        ans = []
        finish = 0 # 已经处理完了的课程数量
        
        while q:
            node = q.popleft()
            ans.append(node)
            finish += 1
            for crs in preMap[node]:
                indegree[crs] -= 1
                if not indegree[crs]:
                    q.append(crs)
        
        if finish != numCourses:
            return []
        return ans

                    
