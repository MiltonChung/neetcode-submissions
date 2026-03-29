class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i: [] for i in range(numCourses)}
        for src, dst in prerequisites:
            adjList[src].append(dst)
        
        visited = set()
        path = set()
        res = []
        self.hasCycle = False

        def dfs(i):
            if i in path:
                self.hasCycle = True
                return
            if i in visited or self.hasCycle:
                return
            path.add(i)

            for neighbor in adjList[i]:
                dfs(neighbor)

            path.remove(i)
            visited.add(i)
            res.append(i)

        for i in range(numCourses):
            if i not in visited:
                dfs(i)
                
        return res if not self.hasCycle else []