class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()
        def dfs(crs):
            if crs in visit:
                return False # detected a cycle
            if preMap[crs] == []:
                return True
            
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            preMap[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True