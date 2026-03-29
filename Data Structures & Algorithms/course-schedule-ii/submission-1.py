class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i: [] for i in range(numCourses)}
        for src, dst in prerequisites:
            adjList[src].append(dst)
        
        res = []
        visited, path = set(), set()
        def dfs(i):
            if i in path:
                return False
            if i in visited:
                return True
            path.add(i)

            for neighbor in adjList[i]:
                if not dfs(neighbor):
                    return False
            
            path.remove(i)
            visited.add(i)
            res.append(i)
            return True
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []
        
        return res