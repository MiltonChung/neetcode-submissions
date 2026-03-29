class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        path = set()
        adjList = {i: [] for i in range(numCourses)}
        for src, dst in prerequisites:
            adjList[src].append(dst)

        def dfs(i):
            if i in path:
                return False
            if i in visited:
                return True
            path.add(i)

            for n in adjList[i]:
                if not dfs(n):
                    return False
            path.remove(i)
            visited.add(i)
            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False
        return True