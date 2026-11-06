class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visiting = set()
        
        def dfs(course):
            if course in visiting:
                return False
            if preMap[course] == []:
                return True
            
            visiting.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            preMap[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True